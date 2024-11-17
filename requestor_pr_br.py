# Импортируем библиотеку, чтобы читаемо представлять данные о дате.
import datetime as dt
# Импортируем метод get из библиотеки requests для получения последних новостей от Банка России.
from requests import get
# Импортируем библиотеку тикей, чтобы представлять данные в красивой графической оболочке
import tkinter as tk

# Создаем функцию для приведения данных о свежих пресс-релизах Банка России, полученных методом get, в читаемый вид.
# Также вводим число интересующих нас пресс-релизовю
def upgrader_html_br(response, number: int):
    # Обрабатываем введенное число для выдачи корректного результата, поскольку будем идти по тегам страницы.
    number_1 = number * 4 + 2
    # Проверяем, что запрос прошел успешно посредством метода status_code.
    if response.status_code == 200:
        # Ставим флаг, чтобы корректно вывести на консоль интересующие нас свежие пресс-релиза.
        flag = 0
        # Создаем три промежуточных списка для сбора данных. Создаем словарь для использования следующей библиотеки Pandas.
        list_titles, list_links, list_dates = [], [], []
        # При помощи метода text переводим данные ответа в текстовый формат и проходим по получившимся строкам.
        for str_i in response.text.split('\n'):
            # Убираем мешающую нам табуляцию со строк.
            str_m = str_i.lstrip()
            # Вычленяем интересующие нас строки по тегам "link" и "title".
            if str_m.startswith('<link>') or str_m.startswith('<title>'):
                flag += 1
                # Первые два тега относятся к общему заголовку страницы и нас не интересуют.
                if flag > 2:
                    # Закидываем в списки интересующие нас строки, предварительно очистив их от ненужных тегов.
                    if str_m.startswith('<title>'):
                        list_titles.append(str_m[7:-22])
                        date_ = dt.datetime.strptime(str_m[-20:-10], '%d.%m.%Y').date()
                        list_dates.append(date_)
                    elif str_m.startswith('<link>'):
                        list_links.append(str_m[6:-8])
                # Поскольку мы считали нужные нам строки, завершаем работу функции.
                if flag == number_1:
                    break
        # Возвращаем словарь для использования при работе с библиотекой Pandas.
        return {'Заголовок': list_titles, 'Ссылка': list_links, 'Дата пресс-релиза': list_dates}

def start():
    # Считываем количество интересующих нас пресс-релизов из соответствующей строки.
    number = int(numbers_of_pr_entry.get())
    # Интересующий нас УРЛ предусмотрительно размещен Банком России во вкладке Технические ресурсы / RSS-каналы.
    url = 'https://cbr.ru/rss/RssPress'
    # Считываем данные посредством метода get.
    response = get(url)
    # Получаем словарь с помощью ранее описанной функции.
    glossia_pr_br = upgrader_html_br(response, number)
    # Запускаем цикл, чтобы пройтись по полученным пресс-релизам
    for i in range(1, number+1):
        # Получаем строковую маску для получения названия переменной, куда будем вставлять данные словаря.
        x = f'pr_{i}_entry'
        # Используем метод глобаль, чтобы перевести строковую маску в читаемое пайтоном название переменной графического интерфейса.
        x = globals().get(x)
        # Очищаем переменную графического интерфейса от ранее находящихся там данных.
        x.delete(0, 'end')
        # Создаем переменную, в которую помещаем интересующие нас данные из словаря.
        z = (glossia_pr_br['Заголовок'][i], '-', glossia_pr_br['Ссылка'][i], '-', glossia_pr_br['Дата пресс-релиза'][i])
        # Вставляем интересующие нас данные из словаря в переменную графического интерфейса.
        x.insert(0, z)

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Пресс релизы Банка России')
    window.geometry('1500x720')
    window.resizable(False, False)

    cong_label = tk.Label(window, text="Привет! Я помощник, позволяющий получить последние пресс-релизы Банка России.")
    cong_label.place(x=50, y=20)

    numbers_of_pr = tk.Label(window, text="Введи число нужных тебе последних пресс-релизов (число от 1 до 10)")
    numbers_of_pr.place(x=50, y=50)
    numbers_of_pr_entry = tk.Entry(window, width=50)
    numbers_of_pr_entry.place(x=50, y=70)

    button_add = tk.Button(window, text="Погнали!", width=10, height=2, command=start)
    button_add.place(x=50, y=90)

    pr_1_label = tk.Label(window, text="Пресс релиз № 1")
    pr_1_label.place(x=50, y=150)
    pr_1_entry = tk.Entry(window, width=230)
    pr_1_entry.place(x=50, y=170)

    pr_2_label = tk.Label(window, text="Пресс релиз № 2")
    pr_2_label.place(x=50, y=190)
    pr_2_entry = tk.Entry(window, width=230)
    pr_2_entry.place(x=50, y=210)

    pr_3_label = tk.Label(window, text="Пресс релиз № 3")
    pr_3_label.place(x=50, y=230)
    pr_3_entry = tk.Entry(window, width=230)
    pr_3_entry.place(x=50, y=250)

    pr_4_label = tk.Label(window, text="Пресс релиз № 4")
    pr_4_label.place(x=50, y=270)
    pr_4_entry = tk.Entry(window, width=230)
    pr_4_entry.place(x=50, y=290)

    pr_5_label = tk.Label(window, text="Пресс релиз № 5")
    pr_5_label.place(x=50, y=310)
    pr_5_entry = tk.Entry(window, width=230)
    pr_5_entry.place(x=50, y=330)

    pr_6_label = tk.Label(window, text="Пресс релиз № 6")
    pr_6_label.place(x=50, y=350)
    pr_6_entry = tk.Entry(window, width=230)
    pr_6_entry.place(x=50, y=370)

    pr_7_label = tk.Label(window, text="Пресс релиз № 7")
    pr_7_label.place(x=50, y=390)
    pr_7_entry = tk.Entry(window, width=230)
    pr_7_entry.place(x=50, y=410)

    pr_8_label = tk.Label(window, text="Пресс релиз № 8")
    pr_8_label.place(x=50, y=430)
    pr_8_entry = tk.Entry(window, width=230)
    pr_8_entry.place(x=50, y=450)

    pr_9_label = tk.Label(window, text="Пресс релиз № 9")
    pr_9_label.place(x=50, y=470)
    pr_9_entry = tk.Entry(window, width=230)
    pr_9_entry.place(x=50, y=490)

    pr_10_label = tk.Label(window, text="Пресс релиз № 10")
    pr_10_label.place(x=50, y=510)
    pr_10_entry = tk.Entry(window, width=230)
    pr_10_entry.place(x=50, y=530)

    window.mainloop()