n = int(input())
found = False
for _ in range(n):
    s = input()
    if 'кот' in s or 'Кот' in s:
        found = True
        break
if found:
    print('МЯУ')
else:
    print('НЕТ')