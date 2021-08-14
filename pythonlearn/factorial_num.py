def factor(n: int) -> int:
    if n <= 1:
        return 1
    return n * factor(n-1)


for i in range(36):
    print(i, factor(i))
