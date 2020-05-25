# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Я выбрал 6 задание 3 урока и протестировал 3 варианта:
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

import timeit
import cProfile
import random

SIZE = 10000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# 1 Python style

def python_style(array):
    min_num = min(array)
    max_num = max(array)
    idx_min = array.index(min_num)
    idx_max = array.index(max_num)

    if idx_min > idx_max:
        idx_min, idx_max = idx_max, idx_min

    summ = 0
    for i in range(idx_min + 1, idx_max):
        summ += array[i]

    return summ


# print(python_style(array))
# print(timeit.timeit('python_style(array)', number=1000, globals=globals())) # SIZE = 100 timeit = 0.011093399999999996
# print(timeit.timeit('python_style(array)', number=1000, globals=globals())) # SIZE = 1000 timeit = 0.18263610000000002
# print(timeit.timeit('python_style(array)', number=1000, globals=globals())) # SIZE = 10000 timeit = 1.0397355
# print(timeit.timeit('python_style(array)', number=1000, globals=globals())) # SIZE = 100000 timeit = 9.2612609
#
#cProfile.run('python_style(array)') # SIZE = 10000 слабых мест не выявлено

print('*' * 50)

#2 Мое решение, где Вы представляли мой ПК с 32Гб ОЗУ:

def last_homework(array):
    min_number = array[0]
    max_number = array[0]
    c = 0
    i = 0

    while i < len(array):
        if array[i] < min_number:
            min_number = array[i]
        if array[i] > max_number:
            max_number = array[i]
        i += 1

    array_3 = array[array.index(min_number):array.index(max_number)]
    array_4 = array[array.index(max_number):array.index(min_number)]

    for i in array_3:
        if i == array_3[0]:
            pass
        else:
            c = i + c
    for i in array_4:
        if i == array_4[0]:
            pass
        else:
            c = i + c
    return c

#print(last_homework(array))

# print(timeit.timeit('last_homework(array)', number=1000, globals=globals())) # SIZE = 100 timeit = 0.06490959999999998
# print(timeit.timeit('last_homework(array)', number=1000, globals=globals())) # SIZE = 1000 timeit = 0.6314346
# print(timeit.timeit('last_homework(array)', number=1000, globals=globals())) # SIZE = 10000 timeit = 7.2340326
# print(timeit.timeit('last_homework(array)', number=1000, globals=globals())) # SIZE = 100000 timeit = мне еще пригодится рабочий ПК
#
# cProfile.run('python_style(array)') # SIZE = 10000 слабых мест не выявлено(в основном все нули. Вывод внизу)


print('*' * 50)

#3 Алгоритмическое

def algorithmic(array):
    idx_min = 0
    idx_max = 0

    for i in range(1, len(array)):
        if array[i] < array[idx_min]:
            idx_min = i
        elif array[i] > array[idx_max]:
            idx_max = i

    if idx_min > idx_max:
        idx_min, idx_max = idx_max, idx_min

    summ = 0
    for i in range(idx_min + 1, idx_max):
        summ += array[i]
    return summ

algorithmic(array)

# print(timeit.timeit('algorithmic(array)', number=1000, globals=globals())) # SIZE = 100 timeit = 0.047227799999999986
# print(timeit.timeit('algorithmic(array)', number=1000, globals=globals())) # SIZE = 1000 timeit = 0.5217187000000001
# print(timeit.timeit('algorithmic(array)', number=1000, globals=globals())) # SIZE = 10000 timeit = 5.0181347999999995
# print(timeit.timeit('algorithmic(array)', number=1000, globals=globals())) # SIZE = 100000 timeit = не буду рисковать
#
# cProfile.run('algorithmic(array)') # SIZE = 10000 / 0.005    0.005    0.005    0.005 HW_04_01.py:93(algorithmic)

# Вывод: Самый быстродейственный вариант получился с функцией # 1 Python style.
# Я так полагаю, что в этом варианте мы используем только один список array и проходимся по нему функциями max и min,
# которые в свою очередь являются итераторами. Ибо во 2 варианте в функции algorithmic() мы задействуем len(),
# которая работает не только с int, но и др типами. Мне кажется, что в данном случае вызов len() дороже по времени,
# чем min и max
# Для сравнения - рейтинг:

print(timeit.timeit('python_style(array)', number=1000, globals=globals())) # SIZE = 10000 timeit = 1.0397355
print(timeit.timeit('algorithmic(array)', number=1000, globals=globals())) # SIZE = 10000 timeit = 5.0181347999999995
print(timeit.timeit('last_homework(array)', number=1000, globals=globals())) # SIZE = 10000 timeit = 7.2340326

