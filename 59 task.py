n = int(input())
total = 0
for _ in range(n):
    x = int(input())
    if x <= 0:
        continue
    total += x
print(total)