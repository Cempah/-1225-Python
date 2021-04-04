def my_func():
    a1 = float(input("Введите число 1: "))
    a2 = float(input("Введите число 2: "))
    while a2 == 0:
        print("Деление на ноль недопустимо. Просьба указать другое значение.")
        a2 = float(input("Введите число 2: "))
    return a1 / a2


print(my_func())