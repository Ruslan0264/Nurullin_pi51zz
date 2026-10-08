login = input('Введите логин:')
mail = input('Введите mail:')
if '@' in mail and '@' not in login:
    print('Ок')
else:print('ОШИБКА')


