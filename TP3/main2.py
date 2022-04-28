import numpy as np
from plotter import plot_error
from simple_perceptron import SimplePerceptron
from utils import Utils, solve_type_step, solve_type_lineal, solve_type_not_lineal

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

correct_set = Utils.escalate(correct_set)
# training_set = Utils.multiple_escalate(training_set)

# min_out = min(correct_set)
# max_out = max(correct_set)

# correct_set = np.array(correct_set)
# correct_set = 2 * (correct_set - min_out) / (max_out - min_out) - 1

[w,errors] = SimplePerceptron(8000).solve(training_set, correct_set, solve_type_lineal)

plot_error(errors)