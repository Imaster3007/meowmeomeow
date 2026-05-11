from models import db, Content
from app import app

with app.app_context():
    db.create_all()

    items = [
        Content(
            title="Парк юрского периода",
            year=1993,
            genre="Фантастика",
            category="Фильм",
            description="Группа учёных посещает парк с клонированными динозаврами.",
            poster="/static/posters/park.png",
            trailer="https://www.youtube.com/watch?v=lc0UehYemQA",
            is_featured=True
        ),
        Content(
            title="Прогулки с динозаврами",
            year=1999,
            genre="Документальный",
            category="Сериал",
            description="Документальный сериал о жизни динозавров.",
            poster="/static/posters/walking_with_dinosaurs.png",
            trailer="https://www.youtube.com/watch?v=G3Vm3N3eBkY",
            is_featured=True
        ),
        Content(
            title="Дино-комикс: Возвращение Тираннозавра",
            year=2018,
            genre="Приключения",
            category="Комикс",
            description="Комикс о приключениях динозавров в современном мире.",
            poster="/static/posters/komiks.png",
            trailer="",
            is_featured=True
        ),
        Content(
            title="Энциклопедия динозавров",
            year=2020,
            genre="Научно-популярная литература",
            category="Энциклопедия",
            description="Подробная энциклопедия о динозаврах с иллюстрациями.",
            poster="/static/posters/pon.png",
            trailer="",
            is_featured=True
        ),
        Content(
            title="Мир юрского периода",
            year=2015,
            genre="Фантастика",
            category="Фильм",
            description="Новый парк с динозаврами выходит из-под контроля.",
            poster="/static/posters/world.png",
            trailer="https://www.youtube.com/watch?v=RFinNxS5KN4",
            is_featured=False
        ),
        Content(
            title="Дино-книга: Тайны мезозоя",
            year=2021,
            genre="Научно-популярная литература",
            category="Книга",
            description="Книга о жизни динозавров в меловом периоде.",
            poster="/static/posters/book.png",
            trailer="",
            is_featured=False
        )
    ]

    db.session.add_all(items)
    db.session.commit()
    print("Контент успешно добавлен!")
