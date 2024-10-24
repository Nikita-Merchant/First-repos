from time import sleep, monotonic
from threading import Thread

class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100
        self.counter_days = 0

    def run(self):
        # if self.flag:
        print(f'{self.name}, на нас напали!')
        while self.enemy > 0:
            sleep(1)
            self.counter_days += 1
            self.enemy -= self.power
            print(f'{self.name} сражается {self.counter_days} день(дня)..., осталось {self.enemy} воинов.')
            if self.enemy <= 0:
                print(f'{self.name} одержал победу спустя {self.counter_days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

if __name__ == '__main__':
    for thr_ in (first_knight, second_knight):
        thr_.start()

    for thr_ in (first_knight, second_knight):
        thr_.join()
    print('Все битвы закончились!')
