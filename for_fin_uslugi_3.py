import tkinter as tk

class WordsFinder:
    def __init__(self, name: str, month: str):
        self.file_name = name
        self.month = month
        self.month_dep_par = {}

    def get_sum(self):
        with open(self.file_name, encoding='utf-8') as file:
            for line in file:
                flag = line.find("'")
                date_ = line[flag+1 : flag+11]
                flag_2 = line.find(')')
                dep_a_inc = [x for x in line[flag+14 : flag_2].split(', ')]
                if line[flag+4:flag+6] == self.month:
                    glos_ = {date_: dep_a_inc}
                    self.month_dep_par.update(glos_)
        return self.month_dep_par.items()

def lesenka_func():
    mask_month = date_entry.get()
    glos_month = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    ex_ = WordsFinder('memory_fin_uslugi.txt', mask_month)
    ex_glos = ex_.get_sum()
    rez = 0
    for key, value in ex_glos:
        for num in value:
            rez += float(num)
    def upgr_month(month):
        if month > 12:
            return f'{glos_month[month - 12]} 2026 года'
        else:
            return f'{glos_month[month]} 2025 года'
    sent_1 = f'Итоговая сумма тел депозитов и процентов в месяце {glos_month[int(mask_month)]}: {round(rez, 2)}'
    sent_2 = 'Вероятное дополнительное поступление: 10 000 руб.'
    sent_3 = 'Следовательно, лесенка должна будет выглядеть следующим образом:'
    sent_4 = f'Первый следующий депозит: {upgr_month(int(mask_month) + 3)}, Размер: {round((rez+10000) / 3, 2)}'
    sent_5 = f'Второй следующий депозит: {upgr_month(int(mask_month) + 6)}, Размер: {round((rez+10000) / 3, 2)}'
    sent_6 = f'Третий следующий депозит: {upgr_month(int(mask_month) + 12)}, Размер: {round((rez+10000) / 3, 2)}'
    sent_1_entry.delete(0, 'end')
    sent_2_entry.delete(0, 'end')
    sent_3_entry.delete(0, 'end')
    sent_4_entry.delete(0, 'end')
    sent_5_entry.delete(0, 'end')
    sent_6_entry.delete(0, 'end')
    sent_1_entry.insert(0, sent_1)
    sent_2_entry.insert(0, sent_2)
    sent_3_entry.insert(0, sent_3)
    sent_4_entry.insert(0, sent_4)
    sent_5_entry.insert(0, sent_5)
    sent_6_entry.insert(0, sent_6)

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Архитектор Лесенки')
    window.geometry('700x700')
    window.resizable(False, False)

    cong_label = tk.Label(window, text="Привет! Я - цифровой архитектор лесенки вкладов! Давай проектировать!")
    cong_label.place(x=100, y=20)

    date_label = tk.Label(window, text='Введи номер месяца в формате "мм": ')
    date_label.place(x=50, y=50)
    date_entry = tk.Entry(window, width=50)
    date_entry.place(x=50, y=70)

    button_add = tk.Button(window, text="Получить рекомендацию архитектора", width=50, height=2, command=lesenka_func)
    button_add.place(x=50, y=120)

    report_label = tk.Label(window, text="Отчет архитектора:")
    report_label.place(x=50, y=160)

    sent_1_entry = tk.Entry(window, width=100)
    sent_1_entry.place(x=50, y=180)
    sent_2_entry = tk.Entry(window, width=100)
    sent_2_entry.place(x=50, y=210)
    sent_3_entry = tk.Entry(window, width=100)
    sent_3_entry.place(x=50, y=240)
    sent_4_entry = tk.Entry(window, width=100)
    sent_4_entry.place(x=50, y=270)
    sent_5_entry = tk.Entry(window, width=100)
    sent_5_entry.place(x=50, y=300)
    sent_6_entry = tk.Entry(window, width=100)
    sent_6_entry.place(x=50, y=330)

    window.mainloop()
