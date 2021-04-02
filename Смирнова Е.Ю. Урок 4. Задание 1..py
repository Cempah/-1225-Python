from sys import argv

script_name, t, s, p = argv
t = int(t)
s = int(s)
p = int(p)


def my_func(t, s, p):
    return (t * s) + p


salary = my_func(t, s, p)
print(f"Заработная плата сотрудника: ", {salary})