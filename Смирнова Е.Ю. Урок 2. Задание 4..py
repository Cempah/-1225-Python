my_str = input("Введите строку из нескольких слов, разделите их пробелами: ").split( )
for i, item in enumerate(my_str):
     print((i + 1), "%.10s" % item)
