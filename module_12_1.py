import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        blade_walker = Runner('Decard')
        for _ in range(10):
            blade_walker.walk()
        self.assertEqual(blade_walker.distance, 50)
    def test_run(self):
        blade_runner = Runner('Roy')
        for _ in range(10):
            blade_runner.run()
        self.assertEqual(blade_runner.distance, 100)
    def test_challenge(self):
        blade_walker_, blade_runner_ = Runner('Rick'), Runner('Butti')
        for _ in range(10):
            blade_walker_.walk()
            blade_runner_.run()
        self.assertNotEqual(blade_runner_.distance, blade_walker_.distance)

if __name__ == '__main__':
    print(unittest.main())