def recurs_fact(n):
    f = 1
    for n in range(1, n+1):
        f *= n
    return f
print(recurs_fact(int(input('Введите факториал: '))))