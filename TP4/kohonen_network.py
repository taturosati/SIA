import math
import numpy as np


class KohonenNetwork:
    def __init__(self, eta, grid_k, radius):
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

        iter_count = len(patterns[0]) * 500 * 5
        final_eta = 0.0001
        final_rad = 1
        dec_eta = (self.eta - final_eta) / iter_count
        dec_rad = (self.radius - final_rad) / iter_count
        
        for _ in range(iter_count):
            pattern = patterns[np.random.choice(len(patterns))]
            winner = self.find_winner(pattern)
            self.update_neighborhood(winner, pattern)
            self.eta -= dec_eta
            self.radius -= dec_rad


    def u_matrix(self):
        avg_weights = np.zeros(shape=(self.grid_k, self.grid_k))
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        for i, row in enumerate(self.weights):
            for j, w in enumerate(row):
                dir_count = 0
                for (dir_x, dir_y) in directions:
                    new_row = dir_x + i
                    new_col = dir_y + j
                    if (new_row >= 0 and new_row < self.grid_k and new_col >= 0 and new_col < self.grid_k):
                        dir_count += 1
                        avg_weights[i][j] += np.linalg.norm(self.weights[new_row][new_col] - w)
                
                avg_weights[i][j] /= dir_count
                
        return avg_weights

    def find_all_winners(self, patterns):
        winners = []
        for pattern in patterns:
            winner = self.find_winner(pattern)
            winners.append(winner)
        
        return winners
    
    
