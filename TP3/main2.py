import numpy as np
from simple_perceptron import SimplePerceptron
from activation import Activation

training_set = []
with open("./training_set.txt", "r") as training_file:
    for line in training_file:
        aux = [float(n) for n in line.split()]
        training_set.append([-1, *aux])
    training_file.close()

correct_set = []
with open("./correct_output.txt", "r") as correct_file:
    for line in correct_file:
        correct_set.append(float(line))
    correct_file.close()

SimplePerceptron(10000).solve(training_set, correct_set, Activation.lineal)