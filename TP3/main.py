from plotter import plot
from simple_perceptron import SimplePerceptron
from activation import Activation

# el -1 al principio de cada ejemplo de entrenamiento es el umbral
and_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
and_out_set = [-1, -1, -1, 1]

print("AND")
SimplePerceptron(1000, 0.0001).solve(and_in_set, and_out_set, Activation.simple)

or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
or_out_set = [1, 1, -1, -1]
print("OR")
SimplePerceptron(50, 0.0001).solve(or_in_set, or_out_set, Activation.simple)
