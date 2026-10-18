prev = input()
while True:
    word = input()
    if word[0] != prev[-1]:
        print(word)
        break
    prev = word