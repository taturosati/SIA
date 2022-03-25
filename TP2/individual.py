import numpy as np
import random


class Individual:
    mutation_probability = 0.05  ##TODO: parametrizar

    def __init__(self, size: int, randomize = True):
        if randomize:
            self.genome = np.random.randint(2, size=size)
        else:
            self.genome = np.empty(size, int)

    def children(self, other, crosser):
        return crosser(self, other)

    def mutate(self):
        for idx, n in enumerate(self.genome):
            mutate = random.random()
            if mutate < Individual.mutation_probability:
                self.genome[idx] = 1 - n

    def calculate_fitness(self, possible_elements, max_elements: int, max_weight: int, absolute_max_weight: int):
        elements = 0
        weight = 0
        gains = 0
        for idx, n in enumerate(self.genome):
            if n == 1:
                elements += 1

            weight += n * possible_elements[idx]["weight"]
            gains += n * possible_elements[idx]["gains"]

        if elements > max_elements or weight > max_weight:
            self.fitness = gains + absolute_max_weight - weight
        else:
            self.fitness = gains + absolute_max_weight

    def __str__(self):
        return str(self.genome)
