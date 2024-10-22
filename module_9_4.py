from random import choice

#Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
rez_1 = map(lambda x, y: x==y, first, second)

#Замыкание
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file_:
            for index_ in range(len(data_set)):
                file_.write(str(data_set[index_]))
                if index_ != len(data_set) - 1:
                    file_.write('\n')
    return write_everything

#Метод __call__
class MysticBall:
    def __init__(self, *words):
        self.words = words
    def __call__(self):
        return choice(self.words)

if __name__ == '__main__':
    print(list(rez_1))
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
    dem_file = open('example.txt', 'r', encoding='utf-8')
    print(dem_file.read())
    dem_file.close()
    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())

