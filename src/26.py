def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed"

# Example usage
result1 = add_numbers(5, 3)
print(result1) # Output: 8
result2 = subtract_numbers(10, 4)
print(result2) # Output: 6

