import factory

from models import db, Content
from app import app





class DinoContentFactory(factory.Factory):

    class Meta:
        model = Content
    
    title = factory.Faker('catch_phrase', locale='ru_RU')
    year = factory.Faker('random_int', min=1967, max=2026)
    genre = factory.Faker('random_element', elements=('Документальный', 'Приключения', 'Боевик', 'Фантастика', 'Научно-популярная литература'))
    category = factory.Faker('random_element', elements=('Фильм', 'Книга', 'Комикс','Динозвар',"Сериал","Энциклопедия"))
    description = factory.Faker('text', max_nb_chars=200, locale='ru_RU')
    poster = factory.LazyFunction(lambda: "/static/posters/dino.png")
   
    trailer = factory.Faker('url')
    is_featured = factory.Faker('boolean')

    

with app.app_context():
     
    db.create_all()
    items_to_add = DinoContentFactory.create_batch(100)
      
    db.session.add_all(items_to_add)

    db.session.commit()



