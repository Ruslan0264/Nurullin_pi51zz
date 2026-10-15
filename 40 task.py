secret = 42

while True:
    n = int(input())
    if n > secret:
        print("МЕНЬШЕ")
    elif n < secret:
        print("БОЛЬШЕ")
    else:
        print("УГАДАЛ!")
        break