def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    # Implement the algorithm here
    pass

try:
    x = int(input("Enter a number: "))
    result = square_root(x)
    print(f"The square root of {x} is {result}")
except ValueError as e:
    print(e)
