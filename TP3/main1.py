from plotter import plot, plot_error
from simple_perceptron import SimplePerceptron
from utils import solve_type_step

# el -1 al principio de cada ejemplo de entrenamiento es el umbral
and_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
and_out_set = [-1, -1, -1, 1]


print("AND")
[r,e] = SimplePerceptron(1000).solve({"in": and_in_set, "out": and_out_set}, {"in": [], "out": []}, solve_type_step)
plot_error(e)

or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
or_out_set = [1, 1, -1, -1]
print("XOR")
[r,e] = SimplePerceptron(50).solve(or_in_set, or_out_set, solve_type_step)
plot_error(e)
