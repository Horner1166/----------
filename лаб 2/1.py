def time_greeting (a, b):
    return f"Good {b}, {a}!"

res = time_greeting(input('Введите имя: '), input('Введите время суток: '))
print(res)
