one = input('Ты любишь горы?')
two = input('Ты любишь жару?')
three = input('Ты любишь снег?')
if one == 'да' and two == 'нет' and three == 'нет':
    print('Твоя страна Исландия!')
elif one == 'нет' and two == 'да' and three == 'нет':
    print('Твоя страна Марокко!')
elif one == 'нет' and two == 'нет' and three == 'да':
    print('Твоя страна Россия!')
