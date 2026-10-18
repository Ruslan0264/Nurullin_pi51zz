whitelist = set()
while True:
    s = input()
    if s == '':
        break
    whitelist.add(s)

while True:
    s = input()
    if s == '':
        break
    if s in whitelist:
        print(s)