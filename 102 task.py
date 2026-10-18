n = int(input())
pairs = []
for _ in range(n):
    name, grade = input().split()
    pairs.append((name, int(grade)))

for name, grade in pairs:
    print(name, grade)

print()

for name, grade in pairs:
    if grade in (4, 5):
        print(name, grade)