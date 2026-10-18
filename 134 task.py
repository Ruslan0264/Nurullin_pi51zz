s = input()
counts = {}
for ch in s:
    if ch != ' ':
        counts[ch] = counts.get(ch, 0) + 1

best = None
best_count = -1
for ch in s:
    if ch != ' ' and counts[ch] > best_count:
        best = ch
        best_count = counts[ch]

print(best)