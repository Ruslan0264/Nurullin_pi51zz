count = 0
answer = -1
while True:
    s = input()
    if s == 'СТОП':
        break
    count += 1
    if answer == -1 and ('кот' in s or 'Кот' in s):
        answer = count
print(answer)