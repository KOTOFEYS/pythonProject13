
import runner1
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner1.Runner('Усейн', 10)
        self.runner_2 = runner1.Runner('Андрей', 9)
        self.runner_3 = runner1.Runner('Ник', 3)


    def test_race3(self):
        race = runner1.Tournament(90,  self.runner_1, self.runner_2, self.runner_3)
        self.all_results = race.start()
        TournamentTest.all_results.update(self.all_results)
        self.assertTrue(self.all_results[len(self.all_results)], 'Ник')
    def test_race1(self):
        race = runner1.Tournament(90,  self.runner_1, self.runner_3)
        self.all_results = race.start()
        TournamentTest.all_results.update(self.all_results)
        self.assertTrue(self.all_results[len(self.all_results)], 'Ник')

    def test_race2(self):
        race = runner1.Tournament(90,  self.runner_2, self.runner_3)
        self.all_results = race.start()
        TournamentTest.all_results.update(self.all_results)
        self.assertTrue( self.all_results[len(self.all_results)],'Ник')


    @classmethod
    def tearDown(cls):
        print(cls.all_results)



