username = input()
allowed = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')

for ch in username:
    if ch not in allowed:
        print(f'Неверный символ: {ch}')
        break
else:
    print('OK')