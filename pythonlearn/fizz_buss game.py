low = 1
high = 100
num = 0


def fizz_buzz(x: int) -> str:
    """

    :rtype: str
    """
    global num
    num = x
    if num % 15 == 0:
        word = "fizz buzz"
        return word
    elif num % 3 == 0:
        word = "fizz"
        return word
    elif num % 5 == 0:
        word = "buzz"
        return word
    else:
        return str(num)


for r in range(low, high+1):
    outp = fizz_buzz(r)
    print(outp)
