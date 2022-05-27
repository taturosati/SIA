import math
import numpy as np


class HopfieldNetwork:
    def __init__(self, eta, limit, grid_k, radius):
        self.limit = limit
        self.eta = eta
        self.grid_k = grid_k
        self.radius = radius