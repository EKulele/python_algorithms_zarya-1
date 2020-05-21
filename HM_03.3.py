# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_number = array[0]
max_number = array[0]

i = 0

while i < len(array):          #Признаюсь, я подсмотрел этот способ в интернете...
    if array[i] < min_number:
        min_number = array[i]

    if array[i] > max_number:
        max_number = array[i]

    i += 1

print(f'{min_number=}')
print(f'{max_number=}')

array.insert(array.index(min_number), max_number)
array.pop(array.index(min_number))
array.insert(array.index(max_number), min_number)
array.pop(array.index(max_number))

print(array)
