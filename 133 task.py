n = int(input())
dictionary = {}
for _ in range(n):
    word, translation = input().split()
    dictionary[word] = translation

query = input()
if query in dictionary:
    print(dictionary[query])
else:
    print('Слово не найдено')