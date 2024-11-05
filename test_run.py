import runner1
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen ,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run_1 = runner1.Runner('Urmas')
        while run_1.walk() in range(10):
            self.assertEqual(run_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run_2 = runner1.Runner('Iihu')
        while run_2.walk() in range(10):
            self.assertEqual(run_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_1 = runner1.Runner('Urmas')
        run_2 = runner1.Runner('Iihu')
        while run_1.walk() and run_2.run() in range(10):

            self.assertNotEqual(run_1.distance, run_2.distance)


if __name__ == '__main__':
    unittest.main()
