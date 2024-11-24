import tkinter as tk

def writer_():
    file_memory_resume = open('memory_fin_uslugi.txt', 'a', encoding='utf-8')
    counter_entry.delete(0, 'end')
    result_brutto_entry.delete(0, 'end')
    date_ = date_entry.get()
    body_, income_ = float(body_entry.get()), float(income_entry.get())
    global counter, bd, inc, sum_
    counter += 1
    counter_entry.insert(0, counter)
    bd, inc, sum_ = bd + body_, inc + income_, round((sum_ + body_ + income_), 2)
    result_brutto_entry.insert(0, [bd, inc, sum_])
    file_memory_resume.write(f'{counter}, {date_, body_, income_}, total_result, {bd, inc, sum_}, \n')
    file_memory_resume.close()
    body_entry.delete(0, 'end')
    income_entry.delete(0, 'end')

if __name__ == '__main__':
    counter, bd, inc, sum_ = 0, 0, 0, 0
    window = tk.Tk()
    window.title('Writer_for_fin_uslugi')
    window.geometry('500x500')
    window.resizable(False, False)

    cong_label = tk.Label(window, text="Hi! I am the Writer_for_fin_uslugi! Go! Go! Go!")
    cong_label.place(x=50, y=20)

    date_label = tk.Label(window, text="Take date")
    date_label.place(x=50, y=50)
    date_entry = tk.Entry(window, width=50)
    date_entry.place(x=50, y=70)

    body_label = tk.Label(window, text="body_deposit")
    body_label.place(x=50, y=90)
    body_entry = tk.Entry(window, width=50)
    body_entry.place(x=50, y=110)

    income_label = tk.Label(window, text="income_deposit")
    income_label.place(x=50, y=130)
    income_entry = tk.Entry(window, width=50)
    income_entry.place(x=50, y=150)

    button_add = tk.Button(window, text="Start", width=10, height=2, command=writer_)
    button_add.place(x=50, y=200)

    counter_label = tk.Label(window, text="Current number!")
    counter_label.place(x=50, y=250)
    counter_entry = tk.Entry(window, width=50)
    counter_entry.place(x=50, y=270)

    result_brutto_label = tk.Label(window, text="Total result for FinUslugi")
    result_brutto_label.place(x=50, y=300)
    result_brutto_entry = tk.Entry(window, width=50)
    result_brutto_entry.place(x=50, y=330)

    window.mainloop()
