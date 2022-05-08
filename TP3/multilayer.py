import numpy as np
from layer import Layer
from utils import Utils

class Multilayer:
    def __init__(self, layer_sizes, pattern_size, eta):
        self.layer_sizes = layer_sizes
        self.layers = []
        for idx, layer_size in enumerate(layer_sizes):
            self.layers.append(Layer(eta, layer_size, (pattern_size if idx == 0 else layer_sizes[idx - 1]) + 1, idx == len(layer_sizes) - 1))

    def solve(self, training_set, test_set, error_bound):
        error = error_bound + 1
        errors = []
        metrics = []
        while error > error_bound:
            training_set["in"], training_set["out"] = Utils.shuffle_two_arrays(training_set["in"], training_set["out"])

            for u in range(len(training_set["in"])):

                current_pattern = training_set["in"][u]
                
                self.layers[0].calculate_v(current_pattern)
                for i in range(1, len(self.layer_sizes)):
                    self.layers[i].calculate_v(self.layers[i - 1].get_output())
                
                self.layers[-1].calculate_last_deltas(training_set["out"][u])
                for i in range(len(self.layer_sizes) - 1, 0, -1):
                    self.layers[i - 1].calculate_delta(self.layers[i].get_weighted_deltas())
                
                error = self.calculate_error(training_set["in"], training_set["out"])
                errors.append(error)
            if len(test_set["in"])>0:
                metrics.append(self.calculate_metric(test_set["in"], test_set["out"]))
        return errors, metrics

    def predict(self, input):
        self.layers[0].calculate_v(input)
        for i in range(1, len(self.layer_sizes)):
            self.layers[i].calculate_v(self.layers[i - 1].get_output())
        return self.layers[-1].get_output()
    
    def calculate_error(self, training_set, correct_outputs):
        tot = 0
        for u in range(len(training_set)):
            self.layers[0].calculate_v(training_set[u])
            for i in range(1, len(self.layer_sizes)):
                self.layers[i].calculate_v(self.layers[i - 1].get_output())
            tot += self.layers[-1].calculate_error(correct_outputs[u])
        return tot / 2

    def calculate_metric(self, test_in, test_out):
        pe = 0
        nope = 0
        for i in range(len(test_out)):
            res = self.predict(test_in[i])
            if (sum([abs(n) for n in np.subtract(test_out[i], np.array(res))]) <= 0.1):
                pe += 1
            else:
                nope += 1
        return pe / (pe + nope)
