import random

def get_random_number(n):
    return random.randint(1, n)

def main():
    print("Hello World")
    print("This is a simple school project.")
    num = get_random_number(10)
    print("The random number is:", num)

if __name__ == "__main__":
    main()
