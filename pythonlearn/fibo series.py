def fibonacci(a):
    """Returning the fibonacci number till `n` th number"""
    if 0 <= a <= 1:
        return a
    n_minus1, n_minus2 = 1,0
    result = None
    for i in range(a-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result


fibonacci(6)
for i in range(6):
    print(i, fibonacci(i))