import unittest

from Lesson_3.module_3_5 import result


#скопированный код с ГитХаба
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed
    def run(self):
        self.distance += self.speed * 2
    def walk(self):
        self.distance += self.speed
    def __str__(self):
        return self.name
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)
    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

#Код тестировочного блока
class TournamentTest(unittest.TestCase):

    # Создаём атрибут класса all_results, применив декоратор класс-метода.
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    # Создаём в атрибутах объекты класса Раннер
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    # Настраиваем красивый вывод итогов тестирования
    @classmethod
    def tearDownClass(cls):
        for val in cls.all_results.values():
            print(val)

    # Реализуем три теста с разными составами бегунов.
    def test_dis_1(self):
        tour_1 = Tournament(90, self.runner_1, self.runner_3)
        new_dict = tour_1.start()
        self.all_results[1] = {key: value.name for key, value in new_dict.items()}
        self.assertTrue(new_dict[max(new_dict.keys())], self.runner_3.name)
    def test_dis_2(self):
        tour_2 = Tournament(90, self.runner_2, self.runner_3)
        new_dict = tour_2.start()
        self.all_results[2] = {key: value.name for key, value in new_dict.items()}
        self.assertTrue(new_dict[max(new_dict.keys())], self.runner_3.name)
    def test_dis_3(self):
        tour_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        new_dict = tour_3.start()
        self.all_results[3] = {key: value.name for key, value in new_dict.items()}
        self.assertTrue(new_dict[max(new_dict.keys())], self.runner_3.name)

if __name__ == '__main__':
    unittest.main()