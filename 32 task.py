first = True

while True:
    n = int(input())
    if n == 0:
        break
    if first:
        print(n, end='')
        first = False
    else:
        print(' ', n, end='', sep='')
print()