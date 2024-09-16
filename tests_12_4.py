import logging
import unittest
import rt_with_exceptions


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "")
    def test_walk(self):
        try:
            way1 = rt_with_exceptions.Runner('Vika', -5)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(10):
                way1.walk()
            self.assertEqual(way1.distance, 50)
        except ValueError:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen, "")
    def test_run(self):
        try:
            way2 = rt_with_exceptions.Runner(10)
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                way2.run()
            self.assertEqual(way2.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    @unittest.skipIf(is_frozen, "")
    def test_challenge(self):
        way3 = rt_with_exceptions.Runner('Lena')
        way4 = rt_with_exceptions.Runner('Roma')
        for _ in range(10):
            way3.walk()
            way4.run()
        self.assertNotEqual(way3.distance, way4.distance)

    logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
