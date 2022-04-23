import math
import numpy as np
from qiskit import algorithms

class Solver:
    def __init__(self, inset, correct_output):
        self.inset = inset
        self.correct_output = correct_output
        self.W = np.array([0, 0, 0])
        self.w = np.array([[0, 0, 0], [0, 0, 0]])
        self.w0 = np.array([0, 0])
        self.w_as_array = np.zeros(11, float)

    @staticmethod
    def g_func(num):
        return math.exp(num)/(1 + math.exp(num))

    @staticmethod
    def f_func(W, w, w0, phi):
        tot = 0
        for j in range(1,3):
            aux = 0
            for k in range(0,3):
                aux += w[j-1][k] * phi[k]
            
            tot += W[j] * Solver.g_func(aux - w0[j - 1])
        return Solver.g_func(tot - W[0])

    def error(self, W, w, w0):
        tot = 0
        for i in range(0,3):
            tot += (self.correct_output[i] - Solver.f_func(W, w, w0, self.inset[i])) ** 2
        
        return tot
        
    def obj_f(self, arr):
        W = [arr[i] for i in range(0,3)]
        w = [[], []]
        w[0] = [arr[i] for i in range(3,6)]
        w[1] = [arr[i] for i in range(6,9)]
        w0 = [arr[i] for i in range(9,11)]
        return self.error(W, w, w0)

    def adam_minimizer(self):
        return algorithms.optimizers.ADAM().optimize(11, self.obj_f, initial_point=self.w_as_array)

    def gradient_minimizer(self):
        return algorithms.optimizers.GradientDescent().optimize(11, self.obj_f, initial_point=self.w_as_array)
    
    def conjugate_gradient_minimizer(self):
        return algorithms.optimizers.CG().optimize(11, self.obj_f, initial_point=self.w_as_array)
