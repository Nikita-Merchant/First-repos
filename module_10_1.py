from time import sleep
from threading import Thread
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file_:
        for num in range(1, word_count + 1):
            file_.write(f'Какое-то слово № {num}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

def gen_thr(num, *args):
    list_thr = []
    for i in range(num):
        maska = Thread(target=write_words, args=args[i])
        list_thr.append(maska)
    return list_thr


if __name__ == '__main__':
    time_start_1 = datetime.now()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    time_end_1 = datetime.now()
    time_res_1 = time_end_1 - time_start_1
    print(time_res_1)

    time_start_2 = datetime.now()
    list_args = ((10, 'example1.txt'), (30, 'example2.txt'), (200, 'example3.txt'), (100, 'example4.txt'))
    thr_first, thr_sec, thr_third, thr_four = gen_thr(4, *list_args)
    thr_first.start()
    thr_sec.start()
    thr_third.start()
    thr_four.start()
    thr_first.join()
    thr_sec.join()
    thr_third.join()
    thr_four.join()
    time_end_2 = datetime.now()
    time_res_2 = time_end_2 - time_start_2
    print(time_res_2)