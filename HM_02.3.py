#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843

a = int(input("Введите число: "))


def super_cicle2(user_number):
    i = 0
    z = 10
    h = 1
    n = 0
    while i < len(str(user_number)):
        c1 = user_number % z // h
        n *= 10
        n += c1
        z *= 10
        h *= 10
        i += 1
    return print(f'Число наоборот {n}')

super_cicle2(a)


