nums = list(map(int, input().split()))
p, q = map(int, input().split())
print(sum(nums[p:q + 1]))