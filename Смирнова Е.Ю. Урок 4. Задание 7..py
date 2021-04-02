def my_func(n):
    f = 1
    for el in range(1, n + 1):
        f = el * f
        yield f


for j in my_func(9):
    print(j)
