def multiply(x, y):
    result = x*y
    return result


answer = multiply(10.5, 4)
print(answer)
print()
for val in range(1,6):
    two_times = multiply(2, val)
    print(two_times)