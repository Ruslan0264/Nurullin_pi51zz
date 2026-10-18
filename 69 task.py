m = int(input())
dishes = []
for _ in range(m):
    dishes.append(input())

n = int(input())
cooked = set()
for _ in range(n):
    for dish in input().split():
        cooked.add(dish)

for dish in dishes:
    if dish not in cooked:
        print(dish)