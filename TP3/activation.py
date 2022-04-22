import math

# TODO: fix, threshohold is implemented on simple_perceptron now
class Activation:
    @staticmethod
    def simple(h, u):
        if h - u < 0:
            return -1

        return 1

    @staticmethod
    def lineal(h, u):
        return h - u

    @staticmethod
    def not_lineal(h, u, b):
        x = h, u
        return math.tanh(b * x)
