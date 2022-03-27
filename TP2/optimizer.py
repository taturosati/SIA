from numpy import array

import numpy as np
from crosser import Crosser
from selector import Selector

from individual import Individual


class Optimizer:
    def __init__(
        self,
        possible_elements: array,
        population_size: int,
        max_elements: int,
        max_weight: int,
        gen: int,
        selector,
        crosser,
        mutation_probability,
    ):
        self.possible_elements = possible_elements
        self.population = np.empty(population_size, Individual)
        self.population_size = population_size
        self.max_elements = max_elements
        self.max_weight = max_weight
        self.selector = selector
        self.crosser = crosser
        self.gen = gen
        self.mutation_probability = mutation_probability
        self.generations = 0
        self.init_population()

    def init_population(self):
        for i in range(self.population_size):
            self.population[i] = Individual(
                len(self.possible_elements), self.mutation_probability
            )
            ##self.population[i].calculate_fitness(self.possible_elements, self.max_elements, self.max_weight)

    def optimize(self):
        absolute_max_weight = 0
        for el in self.possible_elements:
            absolute_max_weight += el["weight"]

        while not self.has_to_stop():
            self.generations += 1
            for individual in self.population:
                individual.calculate_fitness(
                    self.possible_elements,
                    self.max_elements,
                    self.max_weight,
                    absolute_max_weight,
                )

            children = []
            while len(children) < self.population_size:
                [first_parent, second_parent] = np.random.choice(
                    self.population, 2, replace=False
                )
                [first_child, second_child] = first_parent.children(
                    second_parent, self.crosser
                )
                first_child.mutate()
                first_child.calculate_fitness(
                    self.possible_elements,
                    self.max_elements,
                    self.max_weight,
                    absolute_max_weight,
                )
                second_child.mutate()
                second_child.calculate_fitness(
                    self.possible_elements,
                    self.max_elements,
                    self.max_weight,
                    absolute_max_weight,
                )
                children.append(first_child)
                children.append(second_child)

            for n in self.population:  # 2*size
                children.append(n)

            children = self.selector(
                children, self.population_size
            )  ##, self.generations)
            for idx, individual in enumerate(children):
                self.population[idx] = individual

        for individual in self.population:
            individual.calculate_fitness(
                self.possible_elements,
                self.max_elements,
                self.max_weight,
                absolute_max_weight,
            )
        print([n.fitness for n in self.population])

    def has_to_stop(self):
        return self.generations > self.gen
