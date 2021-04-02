from itertools import count
from itertools import cycle

n = int(input('Введите начальное значение: '))
a = int(input('Введите конечное значение: '))

for el in count(int(n)):
    if el > a:
        break
    else:
        print(el)

my_list = ['one', 'two', 'three', 'four']
count = 0
f = int(input('Введите максимальное количество строк для выводимого списка: '))
for el in cycle(my_list):
    if count >= f:
        break
    else:
        print(el)
        count += 1
