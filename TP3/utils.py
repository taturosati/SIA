import math
import numpy as np

class Utils:

    @staticmethod
    def activation_simple(h): # math.isclose(h, 0, rel_tol=1e-5) 
        return 1 if h >= 0 else -1

    @staticmethod
    def activation_lineal(h):
        return h

    @staticmethod
    def activation_not_lineal(h):
        return math.tanh(0.5 * h)

    # x -> conjunto de entrenamiento
    # y -> salida deseada
    @staticmethod
    def calculate_step_error(x, y, w, p):
        error = 0
        for i in range(p):
            output = Utils.activation_simple(np.dot(x[i], w))
            error += abs(output - y[i])
        return error
    
    @staticmethod
    def calculate_lineal_error(x, y, w, p):
        error = 0
        for u in range(p):
            aux = np.dot(w, x[u])
            error += (y[u] - aux) ** 2
        return 0.5 * error
    
    @staticmethod
    def calculate_not_lineal_error(x, y, w, p):
        error = 0
        for u in range(p):
            aux = np.dot(w, x[u])
            error += ((y[u]) - Utils.g(aux)) ** 2
        return 0.5 * error
    
    # @staticmethod
    # def escalate(y):
    #     return 2*(y - min(y))/(max(y)-min(y)) - 1

    @staticmethod
    def g(h):
        return math.tanh(h * 0.5)

    @staticmethod
    def g_prima(h):
        return 0.5 *(1 - math.tanh(0.5 * h)**2)

solve_type_step = {"error": Utils.calculate_step_error, "activation": Utils.activation_simple, "mult": 1}
solve_type_lineal = {"error": Utils.calculate_lineal_error, "activation": Utils.activation_lineal, "mult": 1}
solve_type_not_lineal = {"error": Utils.calculate_not_lineal_error, "activation": Utils.activation_not_lineal, "mult": Utils.g_prima}