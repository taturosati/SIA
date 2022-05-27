import numpy as np

class OjaRule:
    def __init__(self, eta, limit):
        self.limit = limit
        self.eta = eta


    def solve(self, in_set):  # training_set: x, correct_output: y
        p = len(in_set)
        iteration = 0
        self.w = np.zeros(len(in_set[0]))

        while iteration < self.limit:
            print(in_set[0])
            a = np.array(in_set)
            indices = np.arange(a.shape[0])
            np.random.shuffle(indices)
            in_set = a[indices]
            print(in_set[0])
            iteration += 1
            for i_x in range(p):
                excitement = np.dot(in_set[i_x], self.w)
                activation = 1 if excitement >= 0 else -1

                for i in range(0, len(self.w)):
                    delta_w = self.eta * (activation * in_set[i] - activation**2 * self.w[i])
                    self.w[i] += delta_w

        return self.w
