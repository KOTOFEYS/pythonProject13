import unittest

import test_run
import test_runner1

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_run.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner1.TournamentTest))

runner = unittest.TextTestRunner(verbosity = 2)
runner.run(runST)