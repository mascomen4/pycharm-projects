class FuzzyBool(float):
    
    def __new__(cls, value = 0.0):
        return super().__new__(cls, value if 0.0 <= value <= 1.0)
    
    def __invert__(self):
        return (1.0 - float(self))

    def __and__(self, other):
        return FuzzyBool(min(self, other))

    def __iand__(self, other):
        return FuzzyBool(min(self, other))

    def __repr__(self):
        return ("{0}({1})".format(self.__class__.__name__, super().__repr__()))
    def __bool__(self):
        return self > 0.5
    def __int__(self):
        return round(self)
