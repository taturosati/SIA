import math
import numpy as np


class KohonenNetwork:
    def __init__(self, eta, limit, grid_k, radius):
        self.limit = limit
        self.eta = eta
        self.grid_k = grid_k
        self.radius = radius

    def init_weights(self, patterns):
        self.weights = np.zeros(shape=(self.grid_k, self.grid_k, len(patterns[0])))
        for i, row in enumerate(self.weights):
            for j, _ in enumerate(row):
                self.weights[i][j] = np.copy(patterns[np.random.choice(len(patterns))])

    def find_winner(self, pattern):
        distance = math.inf
        winner = None

        for i, row in enumerate(self.weights):
            for j, w in enumerate(row):
                if np.linalg.norm(w - pattern) < distance:
                    winner = (i, j)

        return winner

    def update_neighborhood(self, winner, pattern):
        for i, row in enumerate(self.weights):
            for j, w in enumerate(row):
                if math.sqrt((winner[0] - i) ** 2 + (winner[1] - j) ** 2) < self.radius:
                    self.weights[i][j] += self.eta * (pattern - self.weights[i][j])

    def solve(self, patterns):
        self.init_weights(patterns)
        self.radius = self.grid_k ** 2
        
        for t in range(len(patterns) * 500):
            self.eta = 1 / (t + 2)  # TODO: tiene que ser menor a 1, pero hay que ver si esta bien

            pattern = patterns[np.random.choice(len(patterns))]
            winner = self.find_winner(pattern)

            self.update_neighborhood(winner, pattern)
            if self.radius > 0:
                self.radius -= 1
