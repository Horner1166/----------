#Условные приветствия

def time_greeting (a, b):
    return f"Good {a}, {b}!"

res = time_greeting(input('Введите время суток: '), input('Введите имя: '))
print(res)
