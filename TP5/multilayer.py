import numpy as np
from scipy import optimize
from utils import Utils
# from qiskit import algorithms

class Multilayer:
    def __init__(self, layer_sizes, pattern_size):
        self.pattern_size = pattern_size
        self.layer_sizes = layer_sizes
        self.weights = []
        for idx, layer_size in enumerate(layer_sizes):
            weights_size = (pattern_size if idx == 0 else (layer_sizes[idx - 1]))
            layer_weights = np.empty(shape=(layer_size, weights_size))
            for i in range(layer_size):
                layer_weights[i] = np.random.uniform(low=-0.5, high=0.5, size=weights_size)
            
            self.weights.append(layer_weights)

    def solve(self, training_set):
        self.training_set = training_set
        weights = self.get_weights()
        new_weights = optimize.minimize(self.calculate_error, self.get_weights(), method='Powell', bounds=[[-1, 1]] * len(weights))
        # new_weights = algorithms.optimizers.ADAM(lr=1).optimize(len(weights), self.calculate_error, initial_point=self.get_weights())

        print(new_weights)
        self.set_weights(new_weights)

    def get_weights(self):
        weights = []
        for layer_weights in self.weights:
            for pattern_weights in layer_weights:
                for w in pattern_weights:
                    weights.append(w)

        return weights

    def set_weights(self, weights):
        i = 0
        for layer_idx, layer_size in enumerate(self.layer_sizes):
            weights_size = (self.pattern_size if layer_idx == 0 else (self.layer_sizes[layer_idx - 1]))
            for perceptron_idx in range(layer_size):
                for weight_idx in range(weights_size):
                    self.weights[layer_idx][perceptron_idx][weight_idx] = weights[i]
                    i += 1

    def calculate_error_aux(self, training_set, correct_outputs):
        tot = 0
        for u in range(len(training_set)):
            prev_outputs = training_set[u]
            for idx, layer_size in enumerate(self.layer_sizes):
                outputs = np.empty(shape=(layer_size))
                for i in range(layer_size):
                    excitement = np.dot(prev_outputs, self.weights[idx][i])
                    activation = Utils.g(excitement)
                    if idx == len(self.layer_sizes) - 1:
                        tot += (correct_outputs[u][i] - activation) ** 2
                    
                    outputs[i] = activation

                prev_outputs = outputs
        
        print(tot/2);
        return tot / 2

    def calculate_error(self, weights):
        self.set_weights(weights)
        return self.calculate_error_aux(self.training_set["in"], self.training_set["out"])
