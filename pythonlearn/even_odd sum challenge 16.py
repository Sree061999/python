def sum_eo(n, t):
    """returning sum of odd numbers if t=o or else returning the sum of even numbers if t=e
    n= limit, t= accepting e or o"""
    if t.casefold() == "e":
        start = 2
    elif t.casefold() == "o":
        start = 1
    else:
        return -1
    return sum(range(start, n, 2))


a = sum_eo(11, "s")
print(a)

numb = [7, 4, 9, 1, 3, 0, 2]
numb.sort(reverse=True)
print(numb)










