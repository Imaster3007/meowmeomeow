# Импорты Flask и библиотек
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
from sqlalchemy import func


# Импорт моделей и базы данных
from models import db, User, Content, Review, Favorite

# ------------------- Настройка приложения -------------------
app = Flask(__name__)
app.secret_key = "super_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dino.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ------------------- Контекст для всех шаблонов -------------------
@app.context_processor
def inject_telegram():
    return dict(telegram_link="https://t.me/dino_log_channel")

# ------------------- Главная страница -------------------
@app.route('/')
def index():
    # Показываем только отмеченные как популярные
    movies = Content.query.filter_by(is_featured=True).limit(6).all()
    favorites = []
    if 'user_id' in session:
        user_id = session['user_id']
        favorites = Favorite.query.filter_by(user_id=user_id).all()
    return render_template('index.html', movies=movies, favorites=favorites)

# ------------------- Каталог -------------------
@app.route('/catalog')
def catalog():
    q = request.args.get('q', '').strip()
    genre = request.args.get('genre', '').strip()
    year = request.args.get('year', '').strip()
    category = request.args.get('category', '').strip()
    page = int(request.args.get('page', 1))
    favorites = []
    if 'user_id' in session:
        user_id = session['user_id']
        favorites = Favorite.query.filter_by(user_id=user_id).all()
    per_page = 12

    query = Content.query
    if q:
       
        query = query.filter(Content.title.ilike(f"%{q[0].upper()+q[1:8]}%"))
        
    if genre:
        query = query.filter(Content.genre == genre)
    if year:
        try:
            y = int(year)
            query = query.filter(Content.year == y)
        except ValueError:
            pass
    if category:
        query = query.filter(Content.category == category)

    total = query.count()
    movies = query.order_by(func.coalesce(Content.year, 0).desc()) \
        .offset((page - 1) * per_page).limit(per_page).all()
    page_count = (total + per_page - 1) // per_page

    return render_template('catalog.html', movies=movies, page=page, page_count=page_count,favorites=favorites)

# ------------------- Страница контента -------------------
@app.route('/movie/<int:id>')
def movie_page(id):
    movie = Content.query.get_or_404(id)
    reviews = Review.query.filter_by(content_id=id).join(User).add_columns(Review.id,Review.user_id,User.username, Review.text, Review.rating).all()
    is_favorite = False
    page = int(request.args.get('page', 1))
    
    per_page = 7
    
    reviews_query = Review.query.filter_by(content_id=id) \
        .join(User) \
        .add_columns(Review.id,Review.user_id,User.username, Review.text, Review.rating)

    total = reviews_query.count()
    page_count = (total + per_page - 1) // per_page

    reviews = reviews_query \
        .offset((page - 1) * per_page) \
        .limit(per_page) \
        .all()


    
    if 'user_id' in session:
        user_id = session['user_id']
        is_favorite = Favorite.query.filter_by(user_id=user_id, content_id=id).first() is not None
    

    return render_template('movie.html', movie=movie, reviews=reviews, is_favorite=is_favorite,page=page,page_count=page_count)
# ------------------- Отзыв под фильмом -------------------
@app.route('/movie/<int:movie_id>/comment', methods=['POST'])
def add_comment(movie_id):
    if 'user_id' not in session:
        flash('Войдите в аккаунт')
        return redirect(request.referrer or url_for('login'))

    text = request.form.get('text', '').strip()
    rating = int(request.form.get('rating', -1))
      
    if not text:
        flash('Отзыв не может быть пустым')
        return redirect(request.referrer)
    
    
    review = Review(
        user_id=session['user_id'],
        content_id=movie_id,
        text=text,
        rating=rating
    )

    db.session.add(review)
    db.session.commit()

    flash('Комментарий добавлен')
    return redirect(url_for('movie_page', id=movie_id))

@app.route('/comment/<int:comment_id>/delete')
def delete_comment(comment_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    review = Review.query.get_or_404(comment_id)

    if review.user_id != session['user_id']:
        flash('Недостаточно прав')
        return redirect(request.referrer or url_for('index'))

    movie_id = review.content_id

    db.session.delete(review)
    db.session.commit()

    flash('Комментарий удалён')
    return redirect(url_for('movie_page', id=movie_id))
    
# ------------------- Добавление/удаление из избранного -------------------
@app.route('/favorite/<int:content_id>')
def favorite(content_id):
    if 'user_id' not in session:
        flash("Сначала войдите в аккаунт")
        return redirect(url_for('login'))
    user_id = session['user_id']
    fav = Favorite.query.filter_by(user_id=user_id, content_id=content_id).first()
    content = Content.query.get_or_404(content_id)
    if fav:
        db.session.delete(fav)
        db.session.commit()
        flash(f"{content.title} удален из избранного")
    else:
        new_fav = Favorite(user_id=user_id, content_id=content_id)
        db.session.add(new_fav)
        db.session.commit()
        flash(f"{content.title} добавлен в избранное")
    #return redirect(url_for('dashboard'))
    return redirect(request.referrer or url_for('index'))

# ------------------- Регистрация -------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        if User.query.filter((User.username==username)|(User.email==email)).first():
            flash("Пользователь с таким именем или email уже существует")
            return redirect(url_for('register'))
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash("Регистрация прошла успешно")
        return redirect(url_for('login'))
    return render_template('register.html')

# ------------------- Вход -------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash("Вы вошли в аккаунт")
            return redirect(url_for('index'))
        else:
            flash("Неверный логин или пароль")
    return render_template('login.html')

# ------------------- Личный кабинет -------------------
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Сначала войдите в аккаунт")
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if user is None:
        session.clear()
        flash("Сессия устарела. Пожалуйста, войдите заново.")
        return redirect(url_for('login'))

    favorites = Favorite.query.filter_by(user_id=user.id).all()
    return render_template('dashboard.html', name=user.username, favorites=favorites)

# ------------------- Выход -------------------
@app.route('/logout')
def logout():
    session.clear()
    flash("Вы вышли из аккаунта")
    return redirect(url_for('index'))

# ------------------- Запуск приложения -------------------
if __name__ == '__main__':
    with app.app_context():
        if not os.path.exists('dino.db'):
            db.create_all()
    app.run(debug=False)
