# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
#

a = input("Слово? ")

def my_hash(text):
    h_list = set()
    for i in range(len(text)):
        if i == 0:
            for j in range(len(text) - 1):
                h_list.add(hash(text[i : j]))
                #print(h_list)
        else:
            for j in range(len(text), i, - 1):
                h_list.add(hash(text[i : j]))

    return len(h_list)

print(my_hash(a))

# ['p', 'a', 'p', 'a']
# p
# p + a
# p + a + p
# a
# a + p
# a + p + a
# v
# v + a
# a