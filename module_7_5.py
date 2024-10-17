import os
import time

directory = '.'

if __name__ == '__main__':
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath =os.getcwd()
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
                  f'Родительская директория: {parent_dir}')