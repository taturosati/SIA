import numpy as np
import sys
from plotter import plot_error, plot_metric
from simple_perceptron import SimplePerceptron
from utils import Utils, solve_type_step, solve_type_lineal, solve_type_not_lineal

def second_excercise(params: dict):
    has_to_escalate = False
    if params["item"] == "a":
        print("Solving for lineal")
        solve_type = solve_type_lineal
    else:
        has_to_escalate = True
        print("Solving for not lineal")
        solve_type = solve_type_not_lineal

    in_set = []
    with open("./training_set.txt", "r") as training_file:
        for line in training_file:
            aux = [float(n) for n in line.split()]
            in_set.append([-1, *aux])
        training_file.close()

    out_set = []
    with open("./correct_output.txt", "r") as correct_file:
        for line in correct_file:
            out_set.append(float(line))
        correct_file.close()

    min_esc = 0
    max_esc = 0
    if has_to_escalate:
        out_set, min_esc, max_esc = Utils.escalate(out_set)

    in_set, out_set = Utils.shuffle_two_arrays(in_set, out_set)

    k = params["k"]
    in_parts = np.array_split(in_set, k)
    out_parts = np.array_split(out_set, k)

    best_metric = [0]
    best_w = []

    for i in range(k):
        training_set_in = []
        training_set_out = []
        for idx, part in enumerate(in_parts):
            if idx != i:
                training_set_in += list(part)
                training_set_out += list(out_parts[idx])

        training_set = {"in": training_set_in, "out": training_set_out}
        test_set = {"in": in_parts[i], "out": out_parts[i]}
        print("[ k =", i, "]:", end=" ")
        w, errors, metrics, weights = SimplePerceptron(params["eta"], params["limit"]).solve(training_set, test_set, solve_type, False)

        if max(metrics) > max(best_metric):
            best_w = w
            best_metric = metrics


        if has_to_escalate:
            escalated_errors = np.array(errors)
            desescaleted_errors = ((escalated_errors + min_esc) * (max_esc - min_esc) / 2) + 1
            errors = desescaleted_errors

        plot_error(errors)


    print('BEST: ' + str(max(best_metric)))
    plot_metric(best_metric, len(best_metric))
