n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

result = []
for i in range(n - 1):
    result.append(nums[i] + nums[i + 1])

print(' '.join(map(str, result)))