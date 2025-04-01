def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot compute average with an empty list.")
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

numbers_list = [10, 20, 30, 40, 50]
average = calculate_average(numbers_list)
print(f"The average of the given numbers is: {average}")
