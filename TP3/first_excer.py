from plotter import plot_error, plot
from simple_perceptron import SimplePerceptron
from utils import solve_type_step
import numpy as np

def first_excercise(params: dict):
    test_set = {"in": [], "out": []}
    training_set = {}
    if params["item"] == "b":
        or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
        or_out_set = [1, 1, -1, -1]

        training_set = {"in": np.copy(or_in_set), "out": np.copy(or_out_set)}
        print("Solving for XOR")

    else:
        # el -1 al principio de cada ejemplo de entrenamiento es el umbral
        and_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
        and_out_set = [-1, -1, -1, 1]
        training_set = {"in": np.copy(and_in_set), "out": np.copy(and_out_set)}

        print("Solving for AND")


    w, e, m, weights = SimplePerceptron(params["eta"], params["limit"]).solve(training_set, test_set, solve_type_step,True)
    plot_error(e)
    plot(training_set["in"], training_set["out"], weights, 'Grafico')

    print("Final W:", w)
