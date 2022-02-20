# from inspect import dignature
from random import randint
from faker import Faker


def rand_radio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt-BR')
# print(signature(fake.random_number))


def make_recipe():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'serving': fake.random_number(digits=2, fix_len=True),
        'serving_unit': 'Porções',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_radio(),
        }
    }
