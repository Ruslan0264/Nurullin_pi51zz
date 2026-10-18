first = set(map(int, input().split()))
second = set(map(int, input().split()))

diff = first ^ second
if diff:
    print(' '.join(map(str, sorted(diff))))
else:
    print('EMPTY')