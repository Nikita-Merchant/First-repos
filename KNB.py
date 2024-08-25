import time
import random

print("Привет, я игра 'камень, ножницы, бумага'")
print("Введите цифру своего хода на счёт 5")
print(" 1: ⛰️\n", "2: 📄\n", "3: ✂️")
start_ = int(input("\nСтартуем?\n0 - нет, 1 - да\n"))

flag = 1
while flag == 1:

    if start_ == 0:
        print("До свидания")
    elif start_ == 1:
        my_step = random.randint(1,3)
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("5")

        your_step = int(input('Ваш ход: '))
        print(your_step, my_step)
        if your_step == 1 and my_step == 1:
            print("⛰️  ⛰️ ️")
            print("Ничья!")
        elif your_step == 1 and my_step == 2:
            print("⛰️  📄 ️")
            print("Вы проиграли(")
        elif your_step == 1 and my_step == 3:
            print("⛰️  ✂️ ️")
            print("Вы выиграли! Поздравляю!")

        elif your_step == 2 and my_step == 2:
            print("📄 📄")
            print("Ничья!")
        elif your_step == 2 and my_step == 3:
            print("📄 ✂️ ️")
            print("Вы проиграли(")
        elif your_step == 2 and my_step == 1:
            print("📄 ⛰️ ️")
            print("Вы выиграли! Поздравляю!")

        elif your_step == 3 and my_step == 3:
            print("✂️ ✂️")
            print("Ничья!")
        elif your_step == 3 and my_step == 1:
            print("✂️ ️ ⛰️ ️")
            print("Вы проиграли(")
        elif your_step == 3 and my_step == 2:
            print("✂️  📄️")
            print("Вы выиграли! Поздравляю!")
        else:
            print("Вы указали неверный символ.")
    start_2 = int(input("\nСыграем еще раз?\n0 - нет, 1 - да\n"))
    if start_2 == 0:
        print("До свидания")
        flag = 0
    elif start_2 == 1:
        continue
    else: print("Вы указали неверный символ.")
