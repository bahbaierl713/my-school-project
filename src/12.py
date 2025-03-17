import random

def get_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result_str = ''
    for i in range(length):
        result_str += random.choice(letters)
    return result_str


if __name__ == "__main__":
    print(get_random_string(10))