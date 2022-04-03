import numpy as np
import random


class Individual:

    def __init__(self, size: int, mutation_probability: int, randomize=True):
        if randomize:
            self.genome = np.random.choice([0, 1], size=size, p=[0.9, 0.1])
        else:
            self.genome = np.empty(size, int)

        self.valid = True
        self.mutation_probability = mutation_probability

    def cross(self, other, crosser):
        return crosser(self, other)

    def mutate(self):
        for idx, n in enumerate(self.genome):
            mutate = random.random()
            if mutate < self.mutation_probability:
                self.genome[idx] = 1 - n

    def is_valid(self):
        return self.valid

    def calculate_fitness(self, possible_elements, max_elements: int,
                          max_weight: int, absolute_max_weight: int):
        elements = 0
        self.weight = 0
        self.gains = 0
        for idx, n in enumerate(self.genome):
            if n == 1:
                elements += 1
                self.weight += possible_elements[idx]["weight"]
                self.gains += possible_elements[idx]["gains"]

        if elements > max_elements or self.weight > max_weight:
            self.fitness = absolute_max_weight - self.weight
            self.valid = False
        else:
            self.fitness = self.gains + absolute_max_weight
            self.valid = True

    def get_mutation_probability(self):
        return self.mutation_probability

    def __str__(self):
        return str(self.genome)
