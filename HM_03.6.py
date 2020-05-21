# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

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

print(f'{min_number=}')
print(f'{max_number=}')


array_3 = array[array.index(min_number):array.index(max_number)]
array_4 = array[array.index(max_number):array.index(min_number)]


for i in array_3:
    if i == array_3[0]:
        pass
    else:
        #print(i)
        c = i + c

for i in array_4:
    if i == array_4[0]:
        pass
    else:
        #print(i)
        c = i + c

print(f'Cумма элементов, находящихся между минимальным и максимальным элементами составляет {c}')


