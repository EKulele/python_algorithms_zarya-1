# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


array2 =[]
array3 = []
max_number = 1
for i in array:
    if array.count(i) > max_number:
        max_number = array.count(i)
        array2.append(i)



print(f'Число/ла {array2} встречаются в массиве {array} чаще всего')








