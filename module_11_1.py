import datetime as dt
# 1. Используем библиотеку requests для получения последних новостей от Банка России, для чего импортируем
# метод get и его производные.
from requests import get

# Создаем функцию для приведения данных о свежих пресс-релизах Банка России, полученных методом get в читаемом виде.
# Также вводим число интересующих нас пресс-релизовю
def upgrader_html_br(response, number: int):
    # Обрабатываем введенное число для выдачи корректного результата, поскольку будем идти по тегам страницы.
    number = number * 4 + 2
    # Проверяем, что запрос прошел успешно посредством метода status_code.
    if response.status_code == 200:
        print(f'{number} cвежих пресс-релиза(ов) от Банка России:')
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
                    # Выводим интересующие нас строки, предварительно очистив их от ненужных тегов.
                    if str_m.startswith('<title>'):
                        print(str_m[7:-9])
                        list_titles.append(str_m[7:-22])
                        date_ = dt.datetime.strptime(str_m[-20:-10], '%d.%m.%Y')
                        list_dates.append(date_)
                    elif str_m.startswith('<link>'):
                        print(str_m[6:-8])
                        list_links.append(str_m[6:-8])
                # Поскольку мы считали нужные нам строки, завершаем работу функции.
                if flag == number:
                    break
        # Возвращаем словарь для использования при работе с библиотекой Pandas.
        return {'Заголовок': list_titles, 'Ссылка': list_links, 'Дата пресс-релиза': list_dates}




if __name__ == '__main__':
    # Интересующий нас УРЛ предусмотрительно размещен Банком России во вкладке Технические ресурсы / RSS-каналы.
    url = 'https://cbr.ru/rss/RssPress'
    # Считываем данные посредством метода get.
    response = get(url)
    data_for_pandas = upgrader_html_br(response, 12)
    print()

    # 2. Импортируем библиотеку Pandas для представления полученных данных.
    import pandas as pd

    # Превращаем словарь в DataFrame, используя метод Pandas, затем выведем срез получившегося фрейма.
    data_frame = pd.DataFrame(data_for_pandas)
    print(data_frame.iloc[4:8])
    # Сохраним полученный фрейм в текстовый файл.
    frame_ = open('data_frame_press_relyse_Bank_of_Russia.txt', 'w', encoding='utf-8')
    frame_.write(str(data_frame))
    frame_.close()
    # Проверим с помощью метода dtypes типы данных во фрейме.
    print(data_frame.dtypes)
    # Используем метод describe для получения предварительных выводов из фрейма, например, самая ранняя и самая поздняя публикации.
    print(data_frame.describe())
    print()

    # 3. Импортируем библиотеку numpy для работы с массивами чисел.
    import numpy as np

    # Сгенерируем два массива из случайных чисел с помощью метода random.randint.
    massive_1 = np.random.randint(-50, 150, size=(5, 5))
    massive_2 = np.random.randint(-150, 50, size=(5, 5))
    # Выведем значения массивов по соответсвующим индексам
    print(massive_1[1][3])
    print(massive_2[3][1])

    # Образуем третий массив путем сложения полученных ранее массивов.
    massive_3 = massive_1 + massive_2
    # Выведем работу методов numpy суммирования, средней арифметической, минимума и максимума для массивов.
    number_mass = 1
    for mass in [massive_1, massive_2, massive_3]:
        print(f'Массив {number_mass}:',
              f'Сумма массива: {mass.sum()}',
              f'Средняя арифметическая массива: {mass.mean()}',
              f'Минимум массива: {mass.min()}',
              f'Максимум массива: {mass.max()}', sep='\n')
        number_mass += 1

    # Объединим, а затем инвертируем / транспонируем получившиеся массивы при помощи методов библиотеки.
    rez_mas = np.vstack((massive_1, massive_2, massive_3))
    print(rez_mas.transpose())














