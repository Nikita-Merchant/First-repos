import tkinter as tk

flag_cap = False

def cap_on():
    global  flag_cap
    flag_cap = True
def cap_off():
    global  flag_cap
    flag_cap = False


def analis_dep():
    if flag_cap:
        p_ = float(sum_dep_entry.get())
        n_ = float(level_entry.get())
        n = int(sum_days_entry.get()) // 30
        result_netto_entry.delete(0, 'end')
        result_netto = round((p_ * (1 + (n_ / 100) / 12) ** n), 2)
        result_netto_entry.insert(0, result_netto)
    else:
        p_ = float(sum_dep_entry.get())
        n_ = float(level_entry.get())
        n = int(sum_days_entry.get())
        result_netto_entry.delete(0, 'end')
        result_netto = round((((p_ * n_ * n / 366) / 100) + p_), 2)
        result_netto_entry.insert(0, result_netto)

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Анализатор депозитов')
    window.geometry("600x600")
    window.configure(bg='silver')
    # window.resizable(width: False, height: False)
    text1 = tk.Label(window, text='Депозит:', height=5, width=20)
    text1.grid(column=1, row=1)
    text1.place(x=50)

    date_label = tk.Label(window, text="Take date for deposit's start:")
    date_label.place(x=50, y=110)
    date_entry = tk.Entry(window, width=50)
    date_entry.place(x=50, y=130)

    level_label = tk.Label(window, text="Take % level:")
    level_label.place(x=50, y=150)
    level_entry = tk.Entry(window, width=50)
    level_entry.place(x=50, y=170)

    sum_days_label = tk.Label(window, text="Take sum of days:")
    sum_days_label.place(x=50, y=190)
    sum_days_entry = tk.Entry(window, width=50)
    sum_days_entry.place(x=50, y=210)

    sum_dep_label = tk.Label(window, text="Take sum of deposit:")
    sum_dep_label.place(x=50, y=230)
    sum_dep_entry = tk.Entry(window, width=50)
    sum_dep_entry.place(x=50, y=250)

    capitalization_label = tk.Label(window, text="Is there capitalization for deposit:")
    capitalization_label.place(x=50, y=370)
    button_capitalization=tk.Button(window, width=10, height=3, text='On', command=cap_on)
    button_capitalization.place(x=50, y=400)
    button_capitalization=tk.Button(window, width=10, height=3, text='Off', command=cap_off)
    button_capitalization.place(x=150, y=400)

    button_add = tk.Button(window, text="Start", width=10, height=1, command=analis_dep)
    button_add.place(x=400, y=110)

    result_netto_label = tk.Label(window, text="Deposit's result:")
    result_netto_label.place(x=400, y=140)
    result_netto_entry = tk.Entry(window, width=30)
    result_netto_entry.place(x=400, y=160)

    # button_select=tkinter.Button(window, width=20, height=3, text='Выбрать файл')
    # button_select.grid(column=1, row=2)
    window.mainloop()