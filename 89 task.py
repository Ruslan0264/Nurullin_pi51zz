n = int(input())
for _ in range(n):
    s = input()
    if s.startswith('####'):
        continue
    elif s.startswith('%%'):
        print(s[2:])
    else:
        print(s)