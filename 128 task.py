s = input()
count = 0
for ch in s:
    if not ch.isspace():
        count += 1
print(count)