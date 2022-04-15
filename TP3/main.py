from simple_perceptron import SimplePerceptron
from activation import Activation

and_in_set = [[-1, 1],[1, -1],[-1, -1],[1, 1]]
and_out_set = [-1, -1, -1, 1]

print("AND")
SimplePerceptron(30, 0.0001,1).solve(and_in_set, and_out_set, Activation.simple)

or_in_set = [[-1, 1],[1, -1],[-1, -1],[1, 1]]
or_out_set = [1, 1, -1, 1]
print("OR")
SimplePerceptron(30, 0.0001, 1).solve(or_in_set, or_out_set, Activation.simple)