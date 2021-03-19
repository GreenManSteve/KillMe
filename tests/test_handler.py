import unittest
from patient.male import Male


class TestHandlerCase(unittest.TestCase):

    def _score_age(self):
        male = Male(20, 20, False, 25, 25)
        score = male.calculate_framingham()
        self.assertEqual(male.score_risk, score)


if __name__ == '__main__':
    unittest.main
