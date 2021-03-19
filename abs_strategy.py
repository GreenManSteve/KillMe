class Screening(object):

    def __init__(self, person):
        self._person = person

    def calculate_framingham(self):
        self._person.calculate_framingham()
        return self._person.score_risk