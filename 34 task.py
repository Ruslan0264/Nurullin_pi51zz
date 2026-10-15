while True:
    t = float(input())
    if t == 0:
        break
    if t < 15.5:
        print("ХОЛОДНО")
    elif t > 28:
        print("ЖАРКО")
    else:
        print("НОРМАЛЬНО")