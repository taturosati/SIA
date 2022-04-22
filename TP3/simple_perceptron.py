import numpy as np
import math

from plotter import plot


class SimplePerceptron:
    def __init__(self, limit):
        self.limit = limit

    def solve(self, training_set, correct_output, activation_func):  # training_set: x, correct_output: y
        p = len(training_set)
        iteration = 0
        eta = 0.5  # tasa de aprendizaje
        w = np.zeros(len(training_set[0]))
        error = 1
        min_error = p * 2
        w_min = np.zeros(len(training_set[0]))
        weights = []

        while error > 0 and iteration < self.limit:
            iteration += 1
            i_x = np.random.randint(0, p)

            excitement = np.dot(training_set[i_x], w)
            activation = activation_func(excitement)

            for i in range(0, len(w)):
                delta_w = eta * (correct_output[i_x] - activation) * training_set[i_x][i] * 1 # self.g_prima(excitement) # TODO modularizar
                w[i] += delta_w


            error = self.calculate_lineal_error(training_set, correct_output, w, p)
            print(error)
            if error < min_error:
                min_error = error
                w_min = w

            weights.append(np.copy(w))
            # print(w)
        
        plot(training_set, correct_output, weights, "Simple Perceptron")

        print("Iteration " + str(iteration))
        # if iteration == self.limit:
        #     w = w_min
        print(error)
        print(w)
        return w

    # x -> conjunto de entrenamiento
    # y -> salida deseada
    @staticmethod
    def calculate_step_error(x, y, w, p, activation_func):
        error = 0
        for i in range(p):
            output = activation_func(np.dot(x[i], w))
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
            error += ((y[u]) - SimplePerceptron.g(aux)) ** 2
        return 0.5 * error

    def g_prima(self, h):
        return 0.5 *(1 - math.tanh(0.5 * h)**2)
    
    @staticmethod
    def g(h):
        return math.tanh(h * 0.5)
