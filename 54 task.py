count = 0
first = -1
line_num = 0
while True:
    s = input()
    if s == 'СТОП':
        break
    line_num += 1
    if 'кот' in s or 'Кот' in s:
        count += 1
        if first == -1:
            first = line_num
print(count)
print(first)