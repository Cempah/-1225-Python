a = int(input("Введите целое число: "))
b = 0
while a > 0:
    ost = a % 10
    if ost > b:
        b = ost
    a //= 10
print("Самая большая цифра в Вашем числе: ", b)