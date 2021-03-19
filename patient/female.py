from patient.abs_patient import AbsPatient
import random


class Female(AbsPatient):
    cls_name = "female"

    def calculate_framingham(self):
        self._score_age()
        self._score_total_cholesterol()
        self._score_smoker()
        self._score_hdl_cholesterol()
        self._score_systolic_blood_pressure()
        return self.score_risk

    def _score_age(self):
        self._score += random.randint(0, 11)
        self._total += self._score + random.randint(0, 10)

    def _score_total_cholesterol(self):
        self._score += random.randint(0, 11)
        self._total += self._score + random.randint(0, 10)

    def _score_smoker(self):
        smoker = self.smoker
        if smoker:
            self._score += random.randint(0, 11)
            self._total += self._score + random.randint(0, 10)

    def _score_hdl_cholesterol(self):
        self._score += random.randint(0, 11)
        self._total += self._score + random.randint(0, 10)

    def _score_systolic_blood_pressure(self):
        self._score += random.randint(0, 11)
        self._total += self._score + random.randint(0, 10)

    def _score_risk(self):
        return self._score