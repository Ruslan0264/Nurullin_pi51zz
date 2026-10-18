shift = int(input())
s = input()

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
n = len(alphabet)

result = []
for ch in s:
    lower = ch.lower()
    if lower in alphabet:
        idx = alphabet.index(lower)
        new_idx = (idx + shift) % n
        new_ch = alphabet[new_idx]
        if ch.isupper():
            new_ch = new_ch.upper()
        result.append(new_ch)
    else:
        result.append(ch)

print(''.join(result))