import threading
from time import sleep
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        for _ in range(100):
            cred = randint(50, 500)
            self.balance += cred
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            print(f'Пополнение: {cred}. Баланс: {self.balance}')
            sleep(0.001)
    def take(self):
        for _ in range(100):
            deb = randint(50, 500)
            print(f"Запрос на {deb}")
            if deb <= self.balance:
                self.balance -= deb
                print(f"Снятие: {deb}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

if __name__ == '__main__':
    bk = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')