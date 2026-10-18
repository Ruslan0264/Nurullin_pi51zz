n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

print(' '.join(str(x * 3) for x in nums))