import unittest

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

#Код тестировочного блока из модуля 12_2
class TournamentTest(unittest.TestCase):
    # Дополняем код атрибутом класса для управления пропуском тестов
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        for val in cls.all_results.values():
            print(val)

    # Дополняем код декораторами для пропуска тестов
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_dis_1(self):
        tour_1 = Tournament(90, self.runner_1, self.runner_3)
        new_dict = tour_1.start()
        self.all_results[1] = {key: value.name for key, value in new_dict.items()}
        self.assertTrue(new_dict[max(new_dict.keys())], self.runner_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_dis_2(self):
        tour_2 = Tournament(90, self.runner_2, self.runner_3)
        new_dict = tour_2.start()
        self.all_results[2] = {key: value.name for key, value in new_dict.items()}
        self.assertTrue(new_dict[max(new_dict.keys())], self.runner_3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_dis_3(self):
        tour_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        new_dict = tour_3.start()
        self.all_results[3] = {key: value.name for key, value in new_dict.items()}
        self.assertTrue(new_dict[max(new_dict.keys())], self.runner_3.name)

#Код тестировочного блока из модуля 12_1
class RunnerTest(unittest.TestCase):
    # Дополняем код атрибутом класса для управления пропуском тестов
    is_frozen = False

    # Дополняем код декораторами для пропуска тестов
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        blade_walker = Runner('Decard')
        for _ in range(10):
            blade_walker.walk()
        self.assertEqual(blade_walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        blade_runner = Runner('Roy')
        for _ in range(10):
            blade_runner.run()
        self.assertEqual(blade_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        blade_walker_, blade_runner_ = Runner('Rick'), Runner('Butti')
        for _ in range(10):
            blade_walker_.walk()
            blade_runner_.run()
        self.assertNotEqual(blade_runner_.distance, blade_walker_.distance)
