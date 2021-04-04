def my_func():
    a1 = int(input("Введите число 1: "))
    a2 = int(input("Введите число 2: "))
    a3 = int(input("Введите число 3: "))
    a4 = min(a1, a2, a3)
    return (a1 + a2 + a3) - a4


print(my_func())