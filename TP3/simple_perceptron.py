import numpy as np
from plotter import plot_metric
from plotter import plot
from utils import Utils, solve_type_lineal


class SimplePerceptron:
    def __init__(self, eta, limit):
        self.limit = limit
        self.eta = eta

    def predict(self, in_set, solve_type: dict):
        excitement = np.dot(in_set, self.w)
        activation = solve_type["activation"](excitement)
        return activation

    def solve(self, training_set, test_set, solve_type: dict, is_stepped):  # training_set: x, correct_output: y
        p = len(training_set["in"])
        errors = []
        iteration = 0
        converge_limit = 10 ** (-6.5)
        self.w = np.zeros(len(training_set["in"][0]))
        # self.w = np.random.uniform(low=-0.5, high=0.5, size=(len(training_set["in"][0])))
        error = 1
        last_error = 1
        min_error = p * 2
        w_min = np.zeros(len(training_set["in"][0]))
        weights = []

        met = []

        while error > 0.001 and iteration < self.limit:
            training_set["in"], training_set["out"] = Utils.shuffle_two_arrays(training_set["in"], training_set["out"])

            iteration += 1
            # i_x = np.random.randint(0, p)

            for i_x in range(p):
                print(training_set["in"][i_x])
                excitement = np.dot(training_set["in"][i_x], self.w)
                activation = solve_type["activation"](excitement)

                for i in range(0, len(self.w)):
                    delta_w = self.eta * (training_set["out"][i_x] - activation) * training_set["in"][i_x][i] * solve_type["mult"](excitement)
                    self.w[i] += delta_w

                error = solve_type["error"](training_set["in"], training_set["out"], self.w, p)
                print(error)
                if solve_type == solve_type_lineal:
                    error = 2 * (error / p)

                errors.append(error)
                weights.append(np.copy(self.w))

                if error < min_error:
                    min_error = error
                    w_min = self.w

                if not is_stepped and abs(last_error - error) < converge_limit:
                    if len(test_set["in"]) > 0:
                        met.append(self.calculate_metric(test_set["in"], test_set["out"], solve_type))
                        print(min(errors))
                    return self.w, errors, met, weights
                last_error = error

            if len(test_set["in"]) > 0:
                met.append(self.calculate_metric(test_set["in"], test_set["out"], solve_type))

        # plot_metric(met, int(iteration/len(training_set["in"])))

        # plot(training_set, correct_output, weights, "Simple Perceptron")

        # print("Iteration " + str(iteration))
        if iteration == self.limit:
            self.w = w_min

        # print("Final error:",error)
        # print("W:", self.w)
        print(min(errors))
        return self.w, errors, met, weights

    def calculate_metric(self, test_in, test_out, solve_type):
        pe = 0
        nope = 0
        for i in range(len(test_out)):
            res = self.predict(test_in[i], solve_type)
            if abs(test_out[i] - res) < 0.05:
                pe += 1
            else:
                nope += 1
        return pe / (pe + nope)
