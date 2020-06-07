#  Написать два алгоритма нахождения i-го по счёту простого числа.
#  Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
#  Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
import timeit
import cProfile

n = 10000
user_number = 500 #Натуральное число на вход
def mega_function(n, user_number):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    for i, item in enumerate(res):
        if i + 1 == user_number:
            c = item

    return c

mega_function(n, user_number)

# print(timeit.timeit('mega_function(100, 5)', number=1000, globals=globals())) # 0.0671676
# print(timeit.timeit('mega_function(1000, 50)', number=1000, globals=globals())) # 1.064192
# print(timeit.timeit('mega_function(10000, 500)', number=1000, globals=globals())) # 11.872425900000001
# cProfile.run('mega_function(n, user_number)') # ничего критичного при действующих n и user_number

# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

n_2 = 10
sieve_2 = [i for i in range(n_2)]
sieve_3 = []
user_number = 4 #Натуральное число на вход

def prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

# print(timeit.timeit('is_prime(5)', number=1000, globals=globals()))
def not_mega_func(sieve_2,user_number):
    for i in sieve_2:
        if i > 1:
            if prime(i) == True:
                sieve_3.append(i)
                for i, item in enumerate(sieve_3):
                    if i + 1 == user_number:
                        c = item
    return c

not_mega_func(sieve_2,user_number)

# print(timeit.timeit('not_mega_func(sieve_2,user_number)', number=1000, globals=globals())) # 2.4718907999999997 при действующих sieve_2,user_number
# cProfile.run('not_mega_func(sieve_2,user_number)') # Вот здесь уже жесть как много слабых мест. Вариант рабочий, но лучше ни нада




