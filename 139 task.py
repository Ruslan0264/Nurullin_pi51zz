n = int(input())
best_name = None
best_grade = -1

for _ in range(n):
    name, grade = input().split()
    grade = int(grade)
    if grade > best_grade:
        best_grade = grade
        best_name = name

print(best_name)