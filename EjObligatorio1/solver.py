import math
import numpy as np
from scipy import optimize

class Solver:
    def __init__(self, inset, correct_output):
        self.inset = inset
        self.correct_output = correct_output
        self.W = np.array([0, 0, 0])
        self.w = np.array([[0, 0, 0], [0, 0, 0]])
        self.w0 = np.array([0, 0])
        # self.w_as_array = np.zeros(11, float)
        self.w_as_array = np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5])

    def g_func(self, num):
        return math.exp(num)/(1 + math.exp(num))

    def f_func(self, W, w, w0, phi):
        sum = 0
        for j in range (1,2):
            aux = 0
            for k in range (0,2):
                aux += w[j][k] * phi[k]
            sum += W[j] * self.g_func(aux - w0[j - 1])
        return self.g_func(sum - W[0])

    def error(self, W, w, w0):
        sum = 0
        for i in range(0,2):
            sum += (self.correct_output[i] - self.f_func(W, w, w0, self.inset[i])) ** 2
        return sum
    
    @staticmethod
    def obj_f(arr, *args):
        W = [arr[i] for i in range(0,2)]
        w = [[], []]
        w[0] = [arr[i] for i in range(3,5)]
        w[1] = [arr[i] for i in range(6,8)]
        w0 = [arr[i] for i in range(9,10)]
        return Solver.error(args[0],W, w, w0)

    def gradient_minimizer(self):

        optimize.minimize(self.error())
    
    def conjugate_gradient_minimizer(self):
        # return optimize.fmin_cg(self.obj_f, self.w_as_array, params)
        return optimize.minimize(self.obj_f, self.w_as_array, (self), method='CG')
        