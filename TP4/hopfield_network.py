import math
import numpy as np


class HopfieldNetwork:
    def __init__(self, size, patterns):
        self.size = size
        self.weights = np.zeros((self.size, self.size))
        self.initialize_weights(patterns)
    
    def initialize_weights(self, patterns):
        for i in range(self.size):
            for j in range(self.size):
                self.weights[i][j] = 0
                if i != j:
                    for k in range(len(patterns)):
                        self.weights[i][j] += patterns[k][i] * patterns[k][j]
                    self.weights[i][j] /= self.size
    
    def solve(self, c):
        prev_states = np.zeros(self.size)
        states = np.copy(c)

        historic_states = []

        while np.not_equal(prev_states, states).any():
            prev_states = np.copy(states)
            historic_states.append(np.copy(states))

            for i in range(self.size):
                h = 0
                for j in range(self.size):
                    if i != j:
                        h += self.weights[i][j] * prev_states[j]

                states[i] = 1 if h > 0 else prev_states[i] if h == 0 else -1
            


        return states, historic_states


        

