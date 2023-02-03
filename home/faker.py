from .models import *
from faker import Faker
fake = Faker()
import random


def generate_random_data(n)->bool:
    [Author.objects.create(
        nickname = fake.name(),
        firstname = fake.name(),
        lastname = fake.name(),
        birth_date = fake.date_this_century()
    ) for i in range(0,n)

    ]

    return True

def queryfunc(id):
    data = Author.objects.get(id = id)
    return data


def generate_data_foriegnkey(n)->bool:
    [Book.objects.create(
        author = queryfunc(fake.pyint(min_value=1, max_value=20, step=1)),
        title = fake.name(),
        category = fake.random_element(elements=("Fiction", "Non-Fiction", "Mystery", "Romance", "Science Fiction", "Fantasy", "Horror", "Comics")),
        published = fake.date_this_century(),
        price = fake.pydecimal(left_digits=2, right_digits=2, positive=True),
        rating = fake.pyint(min_value=1, max_value=5, step=1)
    ) for i in range(0,n)

    ]

    return True




