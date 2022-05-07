from perceptron import Perceptron


class ThresholdPerceptron(Perceptron):
    def get_activation(self):
        return -1
