nums = list(map(int, input().split()))
result = [x * x for x in nums if x % 2 != 0 and (x * x) % 10 != 9]
print(' '.join(map(str, result)))