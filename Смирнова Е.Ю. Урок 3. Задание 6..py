def int_func(s):
    for i in range(len(s)):
        s[i] = s[i].title()
    return " ".join(s)


s1 = input("Введите слова из маленьких латинских букв: ").split()
print(int_func(s1))