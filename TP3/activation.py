import math

class Activation:
    @staticmethod
    def simple(h): # math.isclose(h, 0, rel_tol=1e-5) 
        return 1 if h >= 0 else -1

    @staticmethod
    def lineal(h):
        return h

    @staticmethod
    def not_lineal(h):
        return math.tanh(0.5 * h)
