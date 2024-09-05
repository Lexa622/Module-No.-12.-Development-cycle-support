import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner("Усэйн", 10)
        self.runner2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner3 = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            result = {}
            for key, value in test_value.items():
                result[key] = value.name
            print(result)

    def test_race1(self):
        race1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        results = race1.start()
        self.all_results[1] = results
        self.assertTrue(results[len(results)].name == "Ник")

    def test_race2(self):
        race2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        results = race2.start()
        self.all_results[2] = results
        self.assertTrue(results[len(results)].name == "Ник")

    def test_race3(self):
        race3 = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = race3.start()
        self.all_results[3] = results
        self.assertTrue(results[len(results)].name == "Ник")
