import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        run_1 = runner.Runner('Urmas')
        while run_1.walk() in range(10):
            self.assertEqual(run_1.distance, 50)

    def test_run(self):
        run_2 = runner.Runner('Iihu')
        while run_2.walk() in range(10):
            self.assertEqual(run_2.distance, 100)

    def test_challenge(self):
        run_1 = runner.Runner('Urmas')
        run_2 = runner.Runner('Iihu')
        while run_1.walk() and run_2.run() in range(10):
            self.assertNotEqual(run_1.distance, run_2.distance)

if __name__ == '__main__':
    unittest.main()