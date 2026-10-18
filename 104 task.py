n = int(input())
lines = []
for _ in range(n):
    lines.append(input())

for line in sorted(lines, key=lambda x: (len(x), x)):
    print(line)