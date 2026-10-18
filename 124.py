words = input().split()
result = []
for w in words:
    result.append('-'.join(w.upper()))
print(' '.join(result))