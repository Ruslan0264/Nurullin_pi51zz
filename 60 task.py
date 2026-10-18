total = 0
count = 0
while True:
    x = int(input())
    if x == 0:
        print('ОК')
        break
    count += 1
    total += x
    if total > 100:
        print('СТОП')
        print(count)
        break