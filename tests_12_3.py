import runner_and_tournament
import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "")
    def test_walk(self):
        way1 = runner.Runner('Vika')
        for _ in range(10):
            way1.walk()
        self.assertEqual(way1.distance, 50)

    @unittest.skipIf(is_frozen, "")
    def test_run(self):
        way2 = runner.Runner('Gera')
        for _ in range(10):
            way2.run()
        self.assertEqual(way2.distance, 100)

    @unittest.skipIf(is_frozen, "")
    def test_challenge(self):
        way3 = runner.Runner('Lena')
        way4 = runner.Runner('Roma')
        for _ in range(10):
            way3.walk()
            way4.run()
        self.assertNotEqual(way3.distance, way4.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.runner1 = runner_and_tournament.Runner("Усэйн", 10)
        self.runner2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner3 = runner_and_tournament.Runner("Ник", 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race1(self):
        race1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        results = race1.start()
        self.all_results[1] = results
        self.assertTrue(results[len(results)].name == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race2(self):
        race2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        results = race2.start()
        self.all_results[2] = results
        self.assertTrue(results[len(results)].name == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race3(self):
        race3 = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = race3.start()
        self.all_results[3] = results
        self.assertTrue(results[len(results)].name == "Ник")
