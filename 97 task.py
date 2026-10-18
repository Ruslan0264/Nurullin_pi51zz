n = int(input())
lines = []
for _ in range(n):
    lines.append(input())
w1 = input()
w2 = input()

for line in lines:
    if w1 in line and w2 in line:
        print(line)