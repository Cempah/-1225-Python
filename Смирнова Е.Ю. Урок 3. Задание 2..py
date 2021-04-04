def my_func(
        name=input("Введите имя: "),
        surname=input("Введите фамилию: "),
        birth_year=input("Введите год рождения: "),
        city=input("Введите город рождения: "),
        email=input("Введите email: "),
        tel_number=input("Введите телефон: ")):
    print(f"Имя: {name}, Фамилия: {surname}, Год рождения: {birth_year}, Город проживания: {city}, Email: {email}, Номер телефона: {tel_number}")


my_func()
