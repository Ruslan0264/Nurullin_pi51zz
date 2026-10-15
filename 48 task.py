n = int(input())
product = 1

for i in range(n):
    x = int(input())
    if x != 0:
        product *= x

print(product)