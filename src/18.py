import random
def random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

random_string(10)
