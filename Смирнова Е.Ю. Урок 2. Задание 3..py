my_dict = {1 : 'Январь', 2 : 'Февраль', 3 : 'Март', 4 : 'Апрель',5 : 'Май',6 : 'Июнь',7 : 'Июль',8 : 'Август',9 : 'Сентябрь',10 : 'Октябрь',11 : 'Ноябрь',12 : 'Декабрь'}
z = [12, 1, 2]
v = [3, 4, 5]
l = [6, 7, 8]
o = [9, 10, 11]
m = int(input("Введите месяц в числовом значении: "))
m1 = my_dict.get(m)
if m in z:
    print("Введённый месяц", m1, "это месяц зимы.")
elif m in v:
    print("Введённый месяц", m1, "это месяц весны.")
elif m in l:
    print("Введённый месяц", m1, "это месяц лета.")
elif m in o:
    print("Введённый месяц", m1, "это месяц осени.")

