import math

import numpy as np


class KohonenNet:
    def __init__(self, eta, limit, grid_k, radius):
        self.limit = limit
        self.eta = eta
        self.grid_k = grid_k
        self.radius = radius

    def init_weights(self, patterns):
        self.weights = np.zeros(shape=(self.grid_k, self.grid_k))
        for row in self.weights:
            for w in row:
                w = np.copy(np.random.choice(patterns, replace=False))

    def find_winner(self, pattern):
        distance = 1  # no se con que inicializarla
        winner = None

        for i, row in enumerate(self.weights):
            for j, w in enumerate(row):
                if np.linalg.norm(w - pattern) < distance:
                    winner = (i, j)

        return winner

    def update_neighborhood(self, winner, pattern):
        for i, row in self.weights:
            for j, w in row:
                if math.sqrt(math.pow(winner[0] - i, 2) + math.pow(winner[1] - j, 2)) < self.radius:
                    w += self.eta * (pattern - w)

        self.radius -= 1

    def solve(self, patterns):
        self.init_weights(patterns)
        self.neighborhood = len(self.grid_k ** 2)

        for t in range(len(patterns) * 500):
            self.eta = 1 / (t + 2)  # TODO: tiene que ser menor a 1, pero hay que ver si esta bien
            pattern = patterns[np.random.choice(patterns, replace=False)]
            winner = self.find_winner(pattern)
            self.update_neighborhood(winner, pattern)
