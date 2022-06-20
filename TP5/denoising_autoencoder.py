from multilayer import Multilayer
import numpy as np
import copy

class DenoisingAutoencoder(Multilayer):
    def __init__(self, layers, n_inputs, noise=0.005):
        super().__init__(layers, n_inputs)
        self.noise = noise

    def calculate_error_aux(self, weights, training_set, correct_outputs):
        new_training_set = copy.deepcopy(training_set)
        for pattern in new_training_set:
            for i in range(len(pattern)):
                if np.random.uniform() < self.noise:
                    pattern[i] = 0 if pattern[i] == 1 else 1
       
        return super().calculate_error_aux(weights, new_training_set, correct_outputs)
