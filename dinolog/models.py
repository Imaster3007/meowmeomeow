# Импорт SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Создание объекта базы данных
db = SQLAlchemy()

# ------------------- Модель пользователя -------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный ID
    username = db.Column(db.String(50), unique=True, nullable=False)  # Имя пользователя
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email
    password = db.Column(db.String(200), nullable=False)  # Хэш пароля
    favorites = db.relationship('Favorite', backref='user', lazy=True)  # Связь с избранным

# ------------------- Модель контента (фильмы/сериалы/книги и т.д.) -------------------
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный ID
    title = db.Column(db.String(200), nullable=False)  # Название
    year = db.Column(db.Integer)  # Год выпуска
    genre = db.Column(db.String(120))  # Жанр
    category = db.Column(db.String(50))  # Категория (Фильм, Сериал, Комикс и т.д.)
    description = db.Column(db.Text)  # Описание
    poster = db.Column(db.String(300))  # Ссылка на постер
    trailer = db.Column(db.String(300))  # Ссылка на трейлер
    is_featured = db.Column(db.Boolean, default=False)  # Показывать на главной

# ------------------- Модель отзыва -------------------
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Автор отзыва
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'))  # К какому контенту
    rating = db.Column(db.Integer)  # Оценка
    text = db.Column(db.Text)  # Текст отзыва

# ------------------- Модель избранного -------------------
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Уникальный ID
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Пользователь
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)  # Контент
    content = db.relationship('Content')  # Связь с объектом Content
