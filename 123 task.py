n = int(input())
for _ in range(n):
    line = input()
    pos = line.find('#')
    if pos != -1:
        line = line[:pos]
    line = line.rstrip()
    if line:
        print(line)