import random

#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1i7BjyaeoBxKMazN9lPbxuqTFdEZkq49P/view?usp=sharing

print("Сумма и произведение цифр трехзначного числа")

a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))

print(f'Сумма чисел {a+b}')
print(f'Произведение чисел {a*b}')

#5.Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

print("На каких местах алфавита стоят буквы")

letters = "abcdefghijklmnopqrstuvwxyz"
first_lt = input("Первая буква ")
second_lt = input("Вторая буква ")

first_lt, second_lt = letters.find(first_lt), letters.find(second_lt)

print(f'Первая буква стоит на {first_lt+1} месте, вторая на {second_lt+1} месте. Между ними {second_lt-first_lt-1} букв/ы')

#4. Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число, ● случайное вещественное число, ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

print("Генератор чего-то и зачем-то")

a = input("Введите 1 что-то")
b = input("Введите 2 что-то")


if a.isdigit() == True:
    a = int(a)
    b = int(b)
    print(random.randint(a, b))

elif a.isalpha() == True:
    print(chr(random.randint(ord(a), ord(b))))

else:
    a = float(a)
    b = float(b)
    print(random.uniform(a,b))


#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print("Найду среднее число из трех")

print("Введите три разных числа: ")
a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = int(input("Введите 3 число: "))

if b < a < c or c < a < b:
    print(f'Среднее число: {a}')
elif a < b < c or c < b < a:
    print(f'Среднее число: {b}')
else:
    print(f'Среднее число: {c}')


#6 Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

print("Номер буквы в алфавите")

a = int(input("Введите порядковый номер буквы: "))

print(chr(a+96))

