import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from faker import Faker
from products.models import Product, Category, ProductImages
import random
import string

def seed_category(n):
    fake = Faker()
    for _ in range(n):
        Category.objects.create(
            name=fake.company(),
            image=f'categories/{fake.image_url()}'
        )

def generate_random_code():
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    numbers = string.digits
    code = random.choice(upper_case) + random.choice(lower_case) + random.choice(numbers)
    all_chars = upper_case + lower_case + numbers
    remaining_length = 8 - len(code)
    code += ''.join(random.choices(all_chars, k=remaining_length))
    random.shuffle(list(code))
    return ''.join(code)

def generate_fake_price(min_price=10.00, max_price=1000.00):
    fake = Faker()
    return round(fake.pyfloat(left_digits=None, right_digits=2, positive=True, min_value=min_price, max_value=max_price), 2)

def seed_product(n):
    fake = Faker()
    categories = list(Category.objects.all())
    images = ['01.jpg', '02.jpg', '03.jpg', '04.jpg', '05.jpg', '06.jpg', '07.jpg', '08.jpg', '09.jpg', '10.jpg']
    for _ in range(n):
        product = Product.objects.create(
            name=fake.name(),
            description=fake.text(max_nb_chars=1000),
            maximum_velocity=str(random.randint(1, 20)),
            electrical_capacity=str(random.randint(1, 20)),
            length=str(random.randint(1, 100)),
            width=str(random.randint(1, 100)),
            height=str(random.randint(1, 100)),
            diameter=str(random.randint(1, 100)),
            size=str(random.randint(1, 100)),
            production_capacity=str(random.randint(1, 100)),
            price=generate_fake_price(100, 100000),
            code=generate_random_code(),
            image=f'products/{random.choice(images)}'
        )
        if categories:
            product.category.add(*random.sample(categories, k=random.randint(1, len(categories))))

# seed_category(5)  # Seed some categories before products
seed_product(90)
