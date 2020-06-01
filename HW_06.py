# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Я выбрал 2 задачу 2 урока. 64 разрядная винда 10, питон 3.8

# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import sys
from collections import deque

array = []
def my_show(object):
    if hasattr(object, '__iter__'):
        if hasattr(object, 'items'):
            for key, value in object.items():
                array.append(sys.getsizeof(object))
                my_show(key)
                my_show(value)

        elif not isinstance(object, str):
            for item in object:
               #c.append(sys.getsizeof(object))
                my_show(item)
    array.append(sys.getsizeof(object))
    result = sum(array)
    return result



# Вариант 1

a = int(input("Введите число: "))
array_2 = []

def super_cicle(user_number):
    i = 0
    z = 10
    h = 1
    count_1 = 0
    count_2 = 0
    while i < len(str(user_number)):
        c1 = user_number % z // h
        if c1 % 2 == 0:
            count_1 += 1
        else:
            count_2 += 1
        z *= 10
        h *= 10
        i += 1
    array_2.extend([i, z, h, count_1 , count_2, c1])

    return f'В числе {a} находится {count_1} четных цифр и {count_2} нечетных. Выделено памяти {my_show(array_2)}'

print(super_cicle(a)) # Выделено памяти 152
print("*" * 50)

# # Вариант 2. Да, это str. И вам, скорей всего, неприятно на это смотреть. Мне тоже.
#
b = input('Введите число: ')
array_3 = []
def super_cicle_2(b):
    count_1 , count_2 = 0 , 0
    for i in b:
        if i in {'0', '2', '4', '6', '8'}:
            count_1 += 1
        else:
            count_2 += 1
    array_3.extend([count_1, count_2, b])
    return f'В числе {b} находится {count_1} четных цифр и {count_2} нечетных. Выделено памяти {my_show(array_3)}'

print(super_cicle_2(b)) # Выделено памяти 263
print("*" * 50)

# Вариант 3. Извращенный. Но что не сделаешь ради исследования памяти

c = deque(input("Введите число: "))
array_4 = []

def mega_var_3(c):
    array = []
    count_1 = 0
    count_2 = 0

    for i in c:
        i = int(i)
        array.append(i)

    for i in array:
        if i % 2 == 0:
            count_1 += 1
        else:
            count_2 += 1
    print(my_show(c))
    print(my_show(count_1))
    print(my_show(count_2))
    array_4.extend([c, count_1, count_2, array])
    return f'В числе {c} находится {count_1} четных цифр и {count_2} нечетных. Выделено памяти {my_show(array_4)}'


print(mega_var_3(c)) # Выделено памяти 1455

# Вывод: лучше всего проработал 1 вариант, тк используется int, вместо str как в других вариантах