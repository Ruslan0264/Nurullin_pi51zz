found = False
while True:
    s = input()
    if s == 'СТОП':
        break
    if 'пёс' in s or 'Пёс' in s:
        found = False
    if 'кот' in s or 'Кот' in s:
        found = True
print('МЯУ' if found else 'НЕТ')