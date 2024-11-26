# Импортируем библиотеку логирования и юниттестов
import logging
import unittest

# Настройка логгирования
logging.basicConfig(filename='runner_tests.log',  filemode='w', level=logging.INFO,
                    format='%(asctime)s // %(levelname)s // %(message)s',  encoding='utf-8')

# Скачанный код с Гитхаба
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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



# Скачанный класс РаннерТеста из предыдущего модуля suite_12_3 (за исключением декораторов)
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            blade_walker = Runner('Decard', -5)
            for _ in range(10):
                blade_walker.walk()
            self.assertEqual(blade_walker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner", exc_info=True)
            return 0

    def test_run(self):
        try:
            blade_runner = Runner(2, 5)
            for _ in range(10):
                blade_runner.run()
            logging.info('"test_run" выполнен успешно')
            self.assertEqual(blade_runner.distance, 100)

        except TypeError as exc:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            return 0

    def test_challenge(self):
        blade_walker_, blade_runner_ = Runner('Rick', 5), Runner('Butti', 8)
        for _ in range(10):
            blade_walker_.walk()
            blade_runner_.run()
        self.assertNotEqual(blade_runner_.distance, blade_walker_.distance)


if __name__ == '__main__':
    unittest.main()


    # first = Runner('Вося', 10)
    # second = Runner('Илья', 5)
    # third = Runner('Арсен', 10)
    #
    # t = Tournament(101, first, second)
    # print(t.start())

