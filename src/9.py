import random
import string
from datetime import date
from faker import Faker
from faker.providers import internet
fake = Faker()

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_email():
    name = fake.name().split(' ')
    domain = generate_random_string(5) + '.com'
    localpart = name[0].lower() + name[1].lower()
    return localpart + '@' + domain

def generate_random_date():
    return date.today()

def generate_random_url():
    return internet.url()