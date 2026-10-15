password = input()
repeat = input()

if len(password) < 8:
    print("Слишком короткий!")
elif password != repeat:
    print("Пароли не совпадают!")
else:
    print("OK")