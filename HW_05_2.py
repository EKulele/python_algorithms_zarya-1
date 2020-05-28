# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘C’, ‘4’, ‘F’]                   [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

numbers = deque([str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F'])
print(numbers)

a = "C7F"
a = a[::-1]
a = deque(a)
b = "FA3"
b = b[::-1]
b = deque(b)

if len(a) > len(b):
    a , b = b , a

result = []
difference = 0

for i in range(len(a)):
    c = numbers.index(a[i]) + numbers.index(b[i]) + difference
    if c > 15:
        d = c - 16
        difference = 1
        result.append(d)
        if i == 2:
            result = result[::-1]
            result.insert(0,1)
    else:
        d = c
        difference = 0
        result.append(d)

print(result)

c_2 = hex(int("C7F", 16) + int("FA3",16))
print(c_2)
