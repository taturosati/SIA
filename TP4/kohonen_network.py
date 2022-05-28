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
                new_dist = np.linalg.norm(pattern - w)
                if new_dist < distance:
                    winner = (i, j)
                    distance = new_dist

        return winner

    def update_neighborhood(self, winner, pattern):
        for i, row in enumerate(self.weights):
            for j, w in enumerate(row):
                if math.sqrt((winner[0] - i) ** 2 + (winner[1] - j) ** 2) < self.radius:
                    self.weights[i][j] += self.eta * (pattern - self.weights[i][j])

    def solve(self, patterns):
        self.init_weights(patterns)
        dec_rate = 3
        rad = self.radius
        eta = self.eta
        
        for t in range(len(patterns[0]) * 500):
            # self.eta = 1 / (t + 2)  # TODO: tiene que ser menor a 1, pero hay que ver si esta bien

            pattern = patterns[np.random.choice(len(patterns))]
            winner = self.find_winner(pattern)

            self.update_neighborhood(winner, pattern)
            # if self.radius > 1:
            self.radius = rad * math.exp(-t/dec_rate)
            self.eta = eta * math.exp(-t/dec_rate)

    def u_matrix(self):
        avg_weights = np.zeros(shape=(self.grid_k, self.grid_k))
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        for i, row in enumerate(self.weights):
            for j, w in enumerate(row):
                for (dir_x, dir_y) in directions:
                    new_row = dir_x + i
                    new_col = dir_y + j
                    if (new_row >= 0 and new_row < self.grid_k and new_col >= 0 and new_col < self.grid_k):
                        avg_weights[i][j] += np.linalg.norm(self.weights[new_row][new_col] - w)
                
                # avg_weights[i][j] /= len(directions)

        return avg_weights / len(directions)
                # if math.sqrt((winner[0] - i) ** 2 + (winner[1] - j) ** 2) < self.radius:
                #     self.weights[i][j] += self.eta * (pattern - self.weights[i][j])

    def find_all_winners(self, patterns):
        winners = []
        for pattern in patterns:
            winner = self.find_winner(pattern)
            winners.append(winner)
        
        return winners
    
    
