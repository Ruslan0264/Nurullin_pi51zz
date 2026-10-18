tokens = input().split()
stack = []
for t in tokens:
    if t in {'+', '-', '*', '/'}:
        b = stack.pop()
        a = stack.pop()
        if t == '+':
            stack.append(a + b)
        elif t == '-':
            stack.append(a - b)
        elif t == '*':
            stack.append(a * b)
        elif t == '/':
            stack.append(a // b)  # целочисленное деление
    else:
        stack.append(int(t))
print(stack[0])