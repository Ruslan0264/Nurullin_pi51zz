n = int(input())
dictionary = {}
for _ in range(n):
    original, translation = input().split()
    dictionary[original] = translation

text = input().split()
result = [dictionary.get(w, w) for w in text]
print(' '.join(result))