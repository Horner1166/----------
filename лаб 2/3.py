def simple_calculator(num1, num2 ,oper):
    result = None
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '/':
        if num2!= 0:
            result = num1 / num2
        else:
            result = "Error"
    elif oper == '*':
        result = num1 * num2
    return result

res = simple_calculator(int(input('Введите число: ')), int(input('Введите число: ')) ,input('Введите оператора: '))
print(res)