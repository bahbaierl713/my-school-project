def square_root(x):
    if x < 0:
        raise ValueError("Square root of negative number is not defined.")
    
    result = x / 2
    
    while True:
        next_result = (result + x / result) / 2
        if abs(next_result - result) < 1e-6: 
            break
        result = next_result

square_root(9)
