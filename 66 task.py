m = int(input())
common = None
for _ in range(m):
    k = int(input())
    students = set()
    for _ in range(k):
        students.add(input())
    if common is None:
        common = students
    else:
        common &= students

for name in sorted(common):
    print(name)