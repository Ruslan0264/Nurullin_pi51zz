s1 = input()
s2 = input()

bulls = 0
for a, b in zip(s1, s2):
    if a == b:
        bulls += 1

# коровы: общие символы с учётом кратности, кроме быков
from collections import Counter
c1 = Counter(s1)
c2 = Counter(s2)
cows = 0
for ch in c1:
    cows += min(c1[ch], c2[ch])
cows -= bulls

print(f'Быки: {bulls}')
print(f'Коровы: {cows}')