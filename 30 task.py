a = int(input('Вводи число первое: '))
b = int(input('Вводи число второе: '))
op = input('Введи операцию (+, -, *, /): ')
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b == 0:
        print('ОШИБКА')
    else:
        print(a / b)
else:
    print('ОШИБКА')