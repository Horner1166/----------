#Факториал с помощью рекурсии

def recurs_fact(n):
    if n == 0:
        return 1
    else:
        return n * recurs_fact(n-1)
print(recurs_fact(int(input('Введите факториал: '))))