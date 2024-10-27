from threading import Thread
from queue import Queue
from random import randint
from time import sleep

class Table:
    def __init__(self, number: int, guest=None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for man in guests:
            flag = 0
            for table in self.tables:
                if table.guest == None:
                    table.guest = man
                    table.guest.start()
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    flag = 1
                    break
            if flag != 1:
                self.queue.put(man)
                print(f'{man.name} в очереди')

    def discuss_guests(self):
        flag_d = 1
        while flag_d:
            if not self.queue.empty() or not all(table.guest for table in self.tables):
                for table in self.tables:
                    if table.guest != None and table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {table.number} свободен')
                        table.guest.join()
                        table.guest = None
                        if not self.queue.empty():
                            man_ = self.queue.get()
                            table.guest = man_
                            print(f'{man_.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                            man_.start()
            else:
                flag_d = 0

if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()