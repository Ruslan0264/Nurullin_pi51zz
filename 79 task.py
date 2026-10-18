s = input()
vowels = 'аеёиоуыэюя'
count = 0
for ch in s.lower():
    if ch in vowels:
        count += 1
print(count)