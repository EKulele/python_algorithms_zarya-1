#В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.

import random

result = random.randint(1, 100)
print(result)
count = 0

while count != 10 :
    user_answer = int(input("Число"))
    if user_answer == result:
        print("U win")
        break
    elif user_answer < result:
        count += 1
        print("Загаданное число больше")
    elif user_answer > result:
        count += 1
        print("Загаданное число меньше")
else:
    print(f'{result=}')
    print("End of count. Sry, dude. U lose")

