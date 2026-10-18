n = int(input())
products = {}
for _ in range(n):
    name, price = input().split()
    products[name] = int(price)

query = input()
if query in products:
    print(products[query])
else:
    print('Товар не найден')