n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

p = int(input())
q = int(input())

print(sum(nums[p:q + 1]))