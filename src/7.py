
import random

def get_random_number(max_value):
    return random.randint(1, max_value)

def get_random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))

def get_random_list(max_value, length):
    return [get_random_number(max_value) for i in range(length)]