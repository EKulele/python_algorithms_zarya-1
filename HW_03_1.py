# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


array = [2,3,4,5,6,7,8,9]

def natural(array):
    count = 0
    for i in range(2, 100):
        if i % array == 0:
            count += 1
    return count

n = 0
for i in array:
    print(f'Натуральному числу {i} кратны {natural(array[n])} чисел')
    n += 1

# Я правильно понял условие?