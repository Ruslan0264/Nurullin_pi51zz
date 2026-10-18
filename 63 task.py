first = set()
while True:
    s = input()
    if s == '':
        break
    first.add(int(s))

second = set()
while True:
    s = input()
    if s == '':
        break
    second.add(int(s))

common = first & second
if common:
    print(' '.join(map(str, common)))
else:
    print('EMPTY')