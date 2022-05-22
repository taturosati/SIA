import math
import numpy as np

class Utils:

    b = 0.8

    @staticmethod
    def set_beta(beta):
        Utils.b = beta

    @staticmethod
    def shuffle_two_arrays(first, second):
        a = np.array(first)
        b = np.array(second)

        indices = np.arange(a.shape[0])
        np.random.shuffle(indices)

        first = a[indices]
        second = b[indices]
        return first, second

    @staticmethod
    def escalate(arr):
        min_out = min(arr)
        max_out = max(arr)

        arr = np.array(arr)
        arr = 2 * (arr - min_out) / (max_out - min_out) - 1
        return arr, min_out, max_out
    
    @staticmethod
    def multiple_escalate(arr):
        for i in range(len(arr)):
            min_out = min(arr[i])
            max_out = max(arr[i])

            arr[i] = np.array(arr[i])
            arr[i] = 2 * (arr[i] - min_out) / (max_out - min_out) - 1
        return arr


    @staticmethod
    def activation_simple(h):
        return 1 if h >= 0 else -1

    @staticmethod
    def activation_lineal(h):
        return h

    @staticmethod
    def activation_not_lineal(h):
        return math.tanh(Utils.b * h)

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

    @staticmethod
    def g(h):
        return math.tanh(Utils.b * h)

    @staticmethod
    def g_prime(h):
        return 0.5 *(1 - math.tanh(Utils.b * h)**2)


ret_one = lambda _: 1

solve_type_step = {"error": Utils.calculate_step_error, "activation": Utils.activation_simple, "mult": ret_one}
solve_type_lineal = {"error": Utils.calculate_lineal_error, "activation": Utils.activation_lineal, "mult": ret_one}
solve_type_not_lineal = {"error": Utils.calculate_not_lineal_error, "activation": Utils.activation_not_lineal, "mult": Utils.g_prime}
