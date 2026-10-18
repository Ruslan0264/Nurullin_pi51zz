n = int(input())
pairs = []
for _ in range(n):
    pos, ch = input().split()
    pairs.append((int(pos), ch))

pairs.sort()
print(''.join(ch for _, ch in pairs))