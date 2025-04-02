def calculate_average(numbers):
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)

average = calculate_average([1.5, 2.5, 3.5, 4.5])
print("The average is:", average)
