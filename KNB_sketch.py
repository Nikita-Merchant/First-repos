import tkinter as tk
import time
import random

def c_step():
    return random.randint(1,3)

def KNB():
    my_step = c_step()
    your_step = int(step_user_entry.get())
    time.sleep(3)
    battle_entry.delete(0, 'end')
    if your_step == 1 and my_step == 1:
        battle_entry.insert(0, "⛰️  ⛰️ ️ - Ничья!")
    elif your_step == 1 and my_step == 2:
        battle_entry.insert(0, "⛰️  📄 ️ - Вы проиграли(")
    elif your_step == 1 and my_step == 3:
        battle_entry.insert(0, '⛰️  ✂️ ️ - Вы выиграли! Поздравляю!')
    elif your_step == 2 and my_step == 2:
        battle_entry.insert(0, "📄 📄 - Ничья!")
    elif your_step == 2 and my_step == 3:
        battle_entry.insert(0, "📄 ✂️ ️ - Вы проиграли(")
    elif your_step == 2 and my_step == 1:
        battle_entry.insert(0, "📄 ⛰️ ️ - Вы выиграли! Поздравляю!")
    elif your_step == 3 and my_step == 3:
        battle_entry.insert(0, '✂️ ✂️ - Ничья!')
    elif your_step == 3 and my_step == 1:
        battle_entry.insert(0, "✂️ ️ ⛰️ - Вы проиграли(")
    elif your_step == 3 and my_step == 2:
        battle_entry.insert(0, "✂️  📄️ - Вы выиграли! Поздравляю!")
    else:
        battle_entry.insert(0, "Вы указали неверный символ.")

window = tk.Tk()
window.title('Камень, ножницы, бумага')
window.geometry('600x600')
window.resizable(False, False)

cong_label = tk.Label(window, text="Привет, я - игра 'камень, ножницы, бумага'")
cong_label.place(x=50, y=50)

step_user_label = tk.Label(window, text="Ваш ход (введите цифру от 1 до 3 \n1: камень - ⛰️\n2: бумага - 📄\n3: ножницы - ✂️")
step_user_label.place(x=50, y=100)
step_user_entry = tk.Entry(window, width=50)
step_user_entry.place(x=50, y=200)

button_add = tk.Button(window, text="Стартуем?", width=10, height=2, command=KNB)
button_add.place(x=50, y=250)
battle_label = tk.Label(window, text="Ход битвы в игре")
battle_label.place(x=50, y=350)
battle_entry = tk.Entry(window, width=50)
battle_entry.place(x=50, y=400)

window.mainloop()