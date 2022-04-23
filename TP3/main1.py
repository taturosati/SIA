from plotter import plot
from simple_perceptron import SimplePerceptron
from utils import solve_type_step

# el -1 al principio de cada ejemplo de entrenamiento es el umbral
and_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
and_out_set = [-1, -1, -1, 1]


print("AND")
SimplePerceptron(1000).solve(and_in_set, and_out_set, solve_type_step)

or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
or_out_set = [1, 1, -1, -1]
print("OR")
SimplePerceptron(50).solve(or_in_set, or_out_set, solve_type_step)
