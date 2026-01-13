#Генератор обратного счета

def cg(num):
    i = num
    print(num)
    if i > 0:
        while i != 1:
            i-= 1
            print(i)
    elif i <= 0:
        print("неверное число")
    return ""
print(cg(int(input('Введите число: '))))