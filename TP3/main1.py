from plotter import plot_error
from simple_perceptron import SimplePerceptron
from utils import solve_type_step

# el -1 al principio de cada ejemplo de entrenamiento es el umbral
and_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
and_out_set = [-1, -1, -1, 1]


print("AND")
w,e,m = SimplePerceptron(1000).solve({"in": and_in_set, "out": and_out_set}, {"in": [], "out": []}, solve_type_step)
plot_error(e)

or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
or_out_set = [1, 1, -1, -1]
print("XOR")
w,e,m = SimplePerceptron(50).solve({"in": or_in_set, "out": or_out_set}, {"in": [], "out": []}, solve_type_step)
plot_error(e)
