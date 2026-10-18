first = []
while True:
    s = input()
    if s == '':
        break
    first.append(s)

second = set()
while True:
    s = input()
    if s == '':
        break
    second.add(s)

for w in first:
    if w not in second:
        print(w)