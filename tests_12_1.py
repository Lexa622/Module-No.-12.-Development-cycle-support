import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        way1 = runner.Runner('Vika')
        for _ in range(10):
            way1.walk()
        self.assertEqual(way1.distance, 50)

    def test_run(self):
        way2 = runner.Runner('Gera')
        for _ in range(10):
            way2.run()
        self.assertEqual(way2.distance, 100)

    def test_challenge(self):
        way3 = runner.Runner('Lena')
        way4 = runner.Runner('Roma')
        for _ in range(10):
            way3.walk()
            way4.run()
        self.assertNotEqual(way3.distance, way4.distance)
