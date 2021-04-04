def my_func(x, y):
    return x ** y


print("Результат возведения в степень первым способом", my_func(2, -1))


def my_func_1(x, y):
    if x == 0:
        return 0
    if y < 0:
        x = 1.0/x
        y = -y
    res = 1
    while y > 0:
        res = res * x
        y = y-1
    return res

print("Результат возведения в степень вторым способом", my_func_1(2, -1))
