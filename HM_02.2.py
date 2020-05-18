# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input("Введите число: "))


def super_cicle(user_number):
    i = 0
    z = 10
    h = 1
    count1 = 0
    count2 = 0
    while i < len(str(user_number)):
        c1 = user_number % z // h
        if c1 % 2 == 0:
            print(f'{c1} четное число')
            count1 += 1
        else:
            print(f'{c1} нечетное число')
            count2 += 1
        z *= 10
        h *= 10
        i += 1
    return print(f'В числе {a} находится {count1} четных цифр и {count2} нечетных')

super_cicle(a)
