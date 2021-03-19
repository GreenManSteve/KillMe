import abc


class NullClass(metaclass=abc.ABCMeta):
    def __init__(self, cls):
        self._cls = cls

    def calculate_framingham(self):
        response = 'No class for {}'.format(self._cls)
        return response
