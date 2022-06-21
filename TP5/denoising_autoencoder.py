from utils import Utils
from multilayer import Multilayer
import numpy as np

class DenoisingAutoencoder(Multilayer):
    def __init__(self, layers, n_inputs, mutation_prob=0.1, max_noise=0.3):
        super().__init__(layers, n_inputs)
        self.max_noise = max_noise
        self.mutation_prob = mutation_prob

    def calculate_error_aux(self, weights, training_set, correct_outputs):
        new_training_set = np.array([Utils.noise_pattern(pattern, self.mutation_prob, self.max_noise) for pattern in training_set])
        return super().calculate_error_aux(weights, new_training_set, correct_outputs)
