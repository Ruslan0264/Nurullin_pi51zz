n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

# пузырьковая сортировка
for i in range(n - 1):
    for j in range(n - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for x in nums:
    print(x)