n = int(input())
names = []
for _ in range(n):
    names.append(input())

from collections import Counter
counts = Counter(names)

total = 0
for name, c in counts.items():
    if c > 1:
        total += c
print(total)