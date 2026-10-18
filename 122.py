nums = list(map(int, input().split()))
p, q = map(int, input().split())
print(sum(x * x for x in nums[p:q + 1]))