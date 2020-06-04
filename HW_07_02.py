# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10

MIN_ITEM = 0
MAX_ITEM = 50

array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] # inuform

print(array)

def merge_sort(left, right):
    array_2 = []
    i , j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array_2.append(left[i])
            i += 1
        else:
            array_2.append(right[j])
            j += 1
    array_2 += left[i:]
    array_2 += right[j:]
    return array_2

def middle_merge(array):
    if len(array) <= 1:
        return array
    middle_arr = len(array) // 2
    left = middle_merge(array[:middle_arr])
    right = middle_merge(array[middle_arr:])
    return merge_sort(left, right)

print(middle_merge(array))




