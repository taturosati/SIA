from perceptron import Perceptron
from utils import Utils
import numpy as np
from threshold_perceptron import ThresholdPerceptron


class Layer:
    def __init__(self, eta, amount_of_perceptrons, amount_of_inputs, is_last_layer):
        self.amount_of_perceptrons = amount_of_perceptrons
        self.amount_of_inputs = amount_of_inputs
        self.perceptrons = [ThresholdPerceptron(eta, amount_of_inputs)] if not is_last_layer else []
        for _ in range(0, self.amount_of_perceptrons):
            self.perceptrons.append(Perceptron(eta, amount_of_inputs))

        if not is_last_layer:
            self.amount_of_perceptrons += 1

    def get_output(self):
        return [p.get_activation() for p in self.perceptrons]

    def calculate_v(self, previous_layer):
        for perceptron in self.perceptrons:
            perceptron.calculate_activation(previous_layer)

    def calculate_last_deltas(self, correct_outputs):
        for i in range(0, len(self.perceptrons)):
            self.perceptrons[i].calculate_last_delta(correct_outputs[i])

    def calculate_delta(self, weighted_deltas):
        for i in range(0, len(self.perceptrons)):
            self.perceptrons[i].calculate_delta(weighted_deltas[i])

    def get_deltas(self):
        return [p.get_delta() for p in self.perceptrons]

    def get_weighted_deltas(self):
        weighted_deltas = np.zeros(self.amount_of_inputs)
        for i in range(self.amount_of_perceptrons):
            # [1, 2] + [3, 4] = [4, 6]
            weighted_deltas += self.perceptrons[i].get_weighted_deltas()

        return weighted_deltas

    def calculate_error(self, correct_output):
        tot = 0
        for i in range(len(correct_output)):
            tot += (correct_output[i] - self.perceptrons[i].get_activation()) ** 2
        return tot
