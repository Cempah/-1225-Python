def my_func():
    a = input("Введите специальный символ, прерывающий прогрмму: ")
    sum = 0
    while True:
        b = input("Введите числа через пробел, разделите их пробелом: ").split()
        try:
            for digit in b:
                sum += int(digit)
            print(f"Сумма введенных чисел равна {sum}")
        except ValueError or b == a:
            print(f"Программа завершена! Итоговая сумма: {sum}")
            return


my_func()