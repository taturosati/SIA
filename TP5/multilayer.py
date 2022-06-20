from logging import exception
import math
import numpy as np
from scipy import optimize
from utils import Utils
from qiskit import algorithms

class Multilayer:
    def __init__(self, layer_sizes, pattern_size):
        self.pattern_size = pattern_size
        layer_sizes = [layer_size + 1 for layer_size in layer_sizes]
        layer_sizes[-1] -= 1
        self.layer_sizes = layer_sizes
        self.input_count = np.empty(shape=(len(layer_sizes)), dtype=int)
        self.input_count[0] = pattern_size
        self.latent_layer_idx = math.floor(len(layer_sizes) / 2)
        for i in range(1, len(layer_sizes)):
            self.input_count[i] = layer_sizes[i - 1]

        self.weights = []
    
        for idx, layer_size in enumerate(layer_sizes):
            weights_size = pattern_size if idx == 0 else layer_sizes[idx - 1]
            layer_weights = np.empty(shape=(layer_size, weights_size))
            for i in range(layer_size):
                layer_weights[i] = np.random.uniform(low=-0.5, high=0.5, size=weights_size)
            
            self.weights.append(layer_weights)

    def solve(self, training_set):
        self.training_set = training_set
        weights = self.get_weights()
        solution = optimize.minimize(
            self.calculate_error, 
            self.get_weights(), 
            method='Powell', 
            bounds=[[-1, 1]] * len(weights),
            options={'maxiter': 50}
        )
        # new_weights = algorithms.optimizers.ADAM().optimize(len(weights), self.calculate_error, initial_point=self.get_weights())

        new_weights = solution['x']
        # print("Final weights", new_weights)
        print("Final error", self.calculate_error(new_weights))

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
            weights_size = self.input_count[layer_idx]
            for perceptron_idx in range(layer_size):
                for weight_idx in range(weights_size):
                    self.weights[layer_idx][perceptron_idx][weight_idx] = weights[i]
                    i += 1

    def calculate_error_aux(self, weights, training_set, correct_outputs):
        tot = 0
        for u in range(len(training_set)):
            encoder_output, weight_start_idx = self.get_encoder_output(weights, training_set[u])
            latent_output, weight_start_idx = self.get_latent_output(weights, encoder_output, weight_start_idx)
            decoder_output, weight_start_idx = self.get_decoder_output(weights, latent_output, weight_start_idx)
            tot += sum((correct_outputs[u] - decoder_output) ** 2)

        print(tot / 2);
        return tot / 2

    def calculate_error(self, weights):
        return self.calculate_error_aux(weights, self.training_set["in"], self.training_set["out"])

    def get_output(self, weights, activation_func, input, layer_start_idx, layer_end_idx, weight_start_idx):
        last_outputs = input
        for layer_idx in range(layer_start_idx, layer_end_idx + 1):
            layer_size = self.layer_sizes[layer_idx]
            outputs = np.empty(shape=(layer_size))
            weight_count = self.input_count[layer_idx]
            for i in range(layer_size):
                excitement = np.dot(last_outputs, weights[weight_start_idx: weight_start_idx + weight_count])
                activation = activation_func(excitement, layer_idx, i)
                outputs[i] = activation
                weight_start_idx += weight_count

            last_outputs = outputs

        return last_outputs, weight_start_idx

    def get_encoder_output(self, weights, input_pattern):
        return self.get_output(weights, self.get_encoder_activation, input_pattern, 0, self.latent_layer_idx - 1, 0)
    
    def get_latent_output(self, weights, encoder_output, weight_start_idx):
        return self.get_output(weights, self.get_latent_activation, encoder_output, self.latent_layer_idx, self.latent_layer_idx, weight_start_idx)

    def get_decoder_output(self, weights, latent_output, weight_start_idx):
        return self.get_output(weights, self.get_decoder_activation, latent_output, self.latent_layer_idx + 1, len(self.layer_sizes) - 1, weight_start_idx)
    
    def get_activation(self, excitement, layer_idx, perceptron_idx, activation_func):
        if layer_idx == len(self.layer_sizes) - 1 or perceptron_idx > 0:
            return activation_func(excitement)
        
        return -1;

    def get_encoder_activation(self, excitement, layer_idx, perceptron_idx):
        return self.get_activation(excitement, layer_idx, perceptron_idx, Utils.activation_sigmoid)

    def get_latent_activation(self, excitement, layer_idx, perceptron_idx):
        return self.get_activation(excitement, layer_idx, perceptron_idx, Utils.activation_sigmoid)
    
    def get_decoder_activation(self, excitement, layer_idx, perceptron_idx):
        return self.get_activation(excitement, layer_idx, perceptron_idx, Utils.activation_sigmoid)

    def get_latent(self, input_pattern):
        encoder_output, weight_start_idx = self.get_encoder_output(self.get_weights(), input_pattern)
        latent_output, weight_start_idx = self.get_latent_output(self.get_weights(), encoder_output, weight_start_idx)
        return latent_output[1:]
    
    def decode(self, input_pattern):
        weight_start_idx = 0
        for layer_idx in range(self.latent_layer_idx + 1):
            weight_start_idx += self.input_count[layer_idx] * self.layer_sizes[layer_idx]
        
        print(weight_start_idx)
        input_pattern = [-1, *input_pattern]
        decoder_output, weight_start_idx = self.get_decoder_output(self.get_weights(), input_pattern, weight_start_idx)
        return decoder_output

    def output(self, input_pattern):
        encoder_output, weight_start_idx = self.get_encoder_output(self.get_weights(), input_pattern)
        latent_output, weight_start_idx = self.get_latent_output(self.get_weights(), encoder_output, weight_start_idx)
        decoder_output, weight_start_idx = self.get_decoder_output(self.get_weights(), latent_output, weight_start_idx)
        return decoder_output

