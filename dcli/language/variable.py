

class Variable():

    def __init__(self, type, name):
        self._type = type
        self._name = name

    @property
    def type(self):
        return self._type

    @property
    def name(self):
        return self._name

