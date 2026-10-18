letter = input().lower()
words = input().split()

for w in words:
    if letter in w.lower():
        print(w)