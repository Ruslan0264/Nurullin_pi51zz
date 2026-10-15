n = int(input())
total = 0

for i in range(n):
    x = int(input())
    if i % 2 == 0:
        total += x
    else:
        total -= x

print(total)