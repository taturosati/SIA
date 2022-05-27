import numpy as np

class OjaRule:
    def __init__(self, eta, limit):
        self.limit = limit
        self.eta = eta


    def solve(self, patterns):  # training_set: x, correct_output: y
        p = len(patterns)
        iteration = 0
        self.w = np.random.uniform(-1, 1, len(patterns[0]))

        while iteration < self.limit:
            a = np.array(patterns)
            indices = np.arange(a.shape[0])
            np.random.shuffle(indices)
            patterns = a[indices]
            iteration += 1
            
            for i_x in range(p):
                excitement = np.dot(patterns[i_x], self.w)
                delta_w = self.eta * excitement * (patterns[i_x] - excitement * self.w)
                self.w += delta_w


                # for j in range(len(self.w)):
                #     delta_w = 0
                #     for i in range(len(patterns)):
                #         delta_w += self.eta * excitement * (patterns[i][j] - excitement * self.w[j])
                    
                #     self.w[j] += delta_w

                # for i in range(0, len(self.w)):
                #     for j in range(0, len(patterns[0])):
                #         delta_w = self.eta * activation * (patterns[i][j] - activation * self.w[j])
                #         self.w[j] += delta_w

        return self.w
