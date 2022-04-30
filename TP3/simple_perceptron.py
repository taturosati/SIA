import numpy as np
from plotter import plot_metric
from plotter import plot

class SimplePerceptron:
    def __init__(self, limit):
        self.limit = limit
    
    def predict(self, in_set, solve_type: dict):
        excitement = np.dot(in_set, self.w)
        activation = solve_type["activation"](excitement)
        return activation

    def solve(self, training_set, test_set, solve_type: dict):  # training_set: x, correct_output: y

        print("p viejo:",len(training_set))
        print("p nuevo:",len(training_set["in"]))
        p = len(training_set["in"])
        errors= []
        iteration = 0
        eta = 0.1  # tasa de aprendizaje
        self.w = np.zeros(len(training_set["in"][0]))
        error = 1
        min_error = p * 2
        w_min = np.zeros(len(training_set["in"][0]))
        weights = []

        met = []
        while error > 0.001 and iteration < self.limit:
            iteration += 1
            i_x = np.random.randint(0, p)

            excitement = np.dot(training_set["in"][i_x], self.w)
            activation = solve_type["activation"](excitement)

            for i in range(0, len(self.w)):
                delta_w = eta * (training_set["out"][i_x] - activation) * training_set["in"][i_x][i] * solve_type["mult"](excitement)
                self.w[i] += delta_w 

            error = solve_type["error"](training_set["in"], training_set["out"], self.w, p)
            errors.append(error)
            if error < min_error:
                min_error = error
                w_min = self.w

            weights.append(np.copy(self.w))

            if iteration % len(training_set["in"]) == 0:
                pe = 0
                nope = 0
                for i in range(len(test_set["out"])):
                    res = self.predict(test_set["in"][i], solve_type)
                    # print(res)
                    if (abs(test_set["out"][i] - res) < 0.01):
                        pe += 1
                        # print("pega")
                    else:
                        # print("no pega")
                        nope += 1
                met.append(pe / (pe + nope))
        
        # plot_metric(met, int(iteration/len(training_set["in"])))

            
                

        
        #plot(training_set, correct_output, weights, "Simple Perceptron")

        # print("Iteration " + str(iteration))
        if iteration == self.limit:
            self.w = w_min

        # print("Final error:",error)
        # print("W:", self.w)
        return self.w, errors, met
