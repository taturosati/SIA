import numpy as np
from plotter import plot_error, plot_metric
from simple_perceptron import SimplePerceptron
from utils import Utils, solve_type_step, solve_type_lineal, solve_type_not_lineal

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

out_set = Utils.escalate(out_set)
# in_set = Utils.multiple_escalate(in_set)

in_set, out_set = Utils.shuffle_two_arrays(in_set, out_set)



# training_len = int(0.8 * len(in_set))
# training_set = {"in": in_set[:training_len], "out": out_set[:training_len]}
# test_set = {"in": in_set[training_len:], "out": out_set[training_len:]}

# # min_out = min(correct_set)
# # max_out = max(correct_set)

# # correct_set = np.array(correct_set)
# # correct_set = 2 * (correct_set - min_out) / (max_out - min_out) - 1

# [w, errors] = SimplePerceptron(8000).solve(training_set, test_set, solve_type_not_lineal)

k = 10
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

    w, errors, metrics = SimplePerceptron(10000).solve(training_set, test_set, solve_type_not_lineal)

    if max(metrics) > max(best_metric):
        best_w = w
        best_metric = metrics

    # plot_error(errors)

print('BEST: ' + str(max(best_metric)))
plot_metric(best_metric, len(best_metric))