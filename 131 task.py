word = input()
counts = {}
order = []
for ch in word:
    if ch not in counts:
        counts[ch] = 0
        order.append(ch)
    counts[ch] += 1

for ch in order:
    print(f'{ch}: {counts[ch]}')