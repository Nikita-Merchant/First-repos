import unittest
import tests_12_3

# Создаем объект ТестСьюта
tournament_and_runner_st = unittest.TestSuite()

# Добавляем в объект ТестСьюта наши тесты
tournament_and_runner_st.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tournament_and_runner_st.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

# Создаем объект Ранер для запуска ТестСьюта
mr_runner = unittest.TextTestRunner(verbosity=2)

if __name__ == '__main__':
    mr_runner.run(tournament_and_runner_st)