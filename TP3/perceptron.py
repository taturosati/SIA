import numpy as np
from utils import Utils

class Perceptron:
    def __init__(self, eta, amount_of_inputs, is_first_layer):
        self.amount_of_inputs = amount_of_inputs
        
        if is_first_layer:
            self.w = np.ones(shape=(amount_of_inputs, 1))
        else:
            self.w = np.random.uniform(low=-0.5, high=0.5, size=(amount_of_inputs))
    
        self.eta = eta
        self.inputs = np.empty(amount_of_inputs)
        self.activation = 0
        self.excitement = 0
        self.delta = 0
    
    def get_weights(self):
        return self.w

    def update_weights(self):
        for i in range(0, self.amount_of_inputs):
            self.w[i] += self.eta * self.inputs[i] * self.delta

    def calculate_last_delta(self, correct_output):
        self.delta = Utils.g_prime(self.excitement) * (correct_output - self.activation)
        self.update_weights()

    def calculate_delta(self, weighted_delta):
        self.delta = Utils.g_prime(self.excitement) * weighted_delta
        self.update_weights()

    def get_delta(self):
        return self.delta
    
    def get_weighted_deltas(self):
        return self.delta * self.w
    
    def calculate_activation(self, previous_activations):
        self.inputs = previous_activations
        self.excitement = np.dot(previous_activations, self.w)
        self.activation = Utils.g(self.excitement)
    
    def get_activation(self):
        return self.activation
