n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    # Убывающая последовательность возможна, только если все числа различны
    if len(nums) == len(set(nums)):
        print('ДА')
    else:
        print('НЕТ')