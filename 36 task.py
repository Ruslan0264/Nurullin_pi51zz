while True:
    password = input()
    repeat = input()

    if len(password) < 8:
        print("Слишком короткий!")
    elif "123" in password:
        print("Содержит 123!")
    elif password != repeat:
        print("Пароли не совпадают!")
    else:
        print("OK")
        break