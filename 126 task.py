s = input().lower()
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1

best = max(counts, key=counts.get)
print(best)