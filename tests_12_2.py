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
        for i, j in cls.all_results.items():
            exit_ = {}
            for k, n in j.items():
                exit_[k] = n.name
            print(exit_)

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


if __name__ == '__main__':
    unittest.main()
