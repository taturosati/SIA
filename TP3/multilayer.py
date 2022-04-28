from pydoc import doc
import numpy as np
from layer import Layer

class Multilayer:
    def __init__(self, layer_sizes, pattern_size, eta): # layer_sizes = [2, 1]
        self.layer_sizes = layer_sizes
        self.layers = []
        for idx, layer_size in enumerate(layer_sizes):
            is_first_layer = idx == 0
            self.layers.append(Layer(eta, layer_size, (pattern_size if idx == 0 else layer_sizes[idx - 1]) + 1, is_first_layer, idx == len(layer_sizes) - 1))

    def solve(self, training_set, correct_outputs, error_bound):
        error = error_bound + 1
        errors = []
        while error > error_bound:
            u = np.random.randint(0, len(training_set))
            current_pattern = training_set[u]
            # print(u)
            
            self.layers[0].calculate_v(current_pattern)
            for i in range(1, len(self.layer_sizes)):
                self.layers[i].calculate_v(self.layers[i - 1].get_output())
            
            self.layers[-1].calculate_last_deltas(correct_outputs[u])
            for i in range(len(self.layer_sizes) - 1, 0, -1):
                self.layers[i - 1].calculate_delta(self.layers[i].get_weighted_deltas())
            
            
            error = self.calculate_error(training_set, correct_outputs)
            errors.append(error)
            # print(error)
        return self.layers[-1].get_output(), errors

    def predict(self, input):
        self.layers[0].calculate_v(input)
        for i in range(1, len(self.layer_sizes)):
            self.layers[i].calculate_v(self.layers[i - 1].get_output())
        return self.layers[-1].get_output()
        
        # self.layers[-1].calculate_last_deltas(correct_outputs[u])
        # for i in range(len(self.layer_sizes) - 1, 0, -1):
        #     self.layers[i - 1].calculate_delta(self.layers[i].get_weighted_deltas())

    
    def calculate_error(self, training_set, correct_outputs):
        tot = 0
        for u in range(len(training_set)):
            self.layers[0].calculate_v(training_set[u])
            for i in range(1, len(self.layer_sizes)):
                self.layers[i].calculate_v(self.layers[i - 1].get_output())
            
            tot += self.layers[-1].calculate_error(correct_outputs[u])
        
        return tot / 2
