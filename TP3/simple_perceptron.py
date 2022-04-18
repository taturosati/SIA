import numpy as np
import math
class SimplePerceptron:
    def __init__(self, cota, error, umbral) -> None:
        self.cota = cota
        self.error = error
        self.umbral = umbral
    def solve(self, in_set, out_set, activation_func): #inset: x, out_set: y 
        p = len(in_set)
        i = 0
        n = 0.1 #tasa de aprendizaje
        w = [0,0] ##np.zeros(n) usa float64 y se rompe todo. ## el umbral se lo paso al pereceptron 
        delta_w = w
        min_error = p*2
        while self.error > 0 and i <self.cota:
            i = i+1
            i_x = np.random.randint(1, p)
            h = self.calculate_h(in_set[i_x], w)
            o = activation_func(h,self.umbral)
            for j in range(0, len(w)):  
                delta_w[j] = n * (out_set[i_x] - o) * in_set[i_x][0] # aca no entiendo que x[i_x] tomar porque seria un array [-1, 1] ponele
                w[j] = w[j] + delta_w[j]
            self.error = self.calculate_error(in_set, out_set, w, p)
            if self.error < min_error:
                min_error = self.error
                w_min = w
            
        if i == self.cota:
            w = w_min
        print(w)
        return w


    def calculate_error(self, x, y, w, p):
        return 0.001
    
    def calculate_h(self,try_i_x, w):
        h = 0
        for i in range(0, len(w)):
            h = try_i_x[i] * w[i]
        return h

