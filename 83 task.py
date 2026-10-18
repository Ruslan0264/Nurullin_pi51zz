s = input()
if s.startswith('Не '):
    print(s[3:])
elif s.startswith('не '):
    print(s[3:])
else:
    print(s)