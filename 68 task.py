m = int(input())
fridge = set()
for _ in range(m):
    fridge.add(input())

n = int(input())
for _ in range(n):
    parts = input().split()
    name = parts[0]
    ingredients = set(parts[1:])
    if ingredients <= fridge:  # все ингредиенты есть в холодильнике
        print(name)