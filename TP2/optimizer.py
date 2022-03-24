from numpy import array

import numpy as np

from individual import Individual

class Optimizer:
    def __init__(self, possible_elements: array, population_size: int, max_elements: int, max_weight: int, selector, crosser):
        self.possible_elements = possible_elements
        self.population = np.empty(population_size, Individual)
        self.population_size = population_size
        self.max_elements = max_elements
        self.max_weight = max_weight
        self.selector = selector
        self.crosser = crosser
        self.generations = 0
        self.init_population()

    def init_population(self): 
        for i in range(self.population_size):
            self.population[i] = Individual(len(self.possible_elements))
            self.population[i].calculate_fitness(self.possible_elements, self.max_elements, self.max_weight)
    
    def optimize(self):
        while not self.has_to_stop():
            self.generations += 1
            for individual in self.population:
                individual.calculate_fitness(self.possible_elements, self.max_elements, self.max_weight)

            children = []
            while len(children) < self.population_size:
                [first, second] = np.random.choice(self.population, 2, replace=False)
                [first_child, second_child] = first.children(second, self.crosser)
                first_child.mutate()
                first_child.calculate_fitness(self.possible_elements, self.max_elements, self.max_weight)
                second_child.mutate()
                second_child.calculate_fitness(self.possible_elements, self.max_elements, self.max_weight)
                children.append(first_child)
                children.append(second_child)

            for n in self.population:
                children.append(n)

            children = self.selector(children, self.population_size)
            for idx, individual in enumerate(children):
                self.population[idx] = individual

        print([n.fitness for n in self.population])

    def has_to_stop(self):
        return self.generations > 500 and len([c for c in self.population if c.fitness > 0]) > 0
                
