n = int(input())
result = []
for _ in range(n):
    s = input()
    if 'лук' not in s:
        result.append(s)
print(', '.join(result))