n = int(input())
for i in range(1, n + 1):
    s = input()
    pos = s.find('кот')
    if pos != -1:
        print(i, pos + 1)