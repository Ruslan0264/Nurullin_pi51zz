n = int(input())
totals = {}
for _ in range(n):
    name, grade = input().split()
    grade = int(grade)
    totals[name] = totals.get(name, 0) + grade

for name, total in totals.items():
    print(f'{name}: {total}')