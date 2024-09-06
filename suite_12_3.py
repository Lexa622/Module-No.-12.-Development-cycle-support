import unittest
import tests_12_3


ran_test = unittest.TestSuite()
ran_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
ran_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(ran_test)
