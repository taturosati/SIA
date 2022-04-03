from numpy import array, average
import time

import numpy as np

from individual import Individual


class Optimizer:
    def __init__(self, possible_elements: array, population_size: int,
                 max_elements: int, max_weight: int, min_generations: int,
                 selector, crosser, mutation_probability):
        self.possible_elements = possible_elements
        self.population = np.empty(population_size, Individual)
        self.population_size = population_size
        self.max_elements = max_elements
        self.max_weight = max_weight
        self.selector = selector
        self.crosser = crosser
        self.min_generations = min_generations
        self.mutation_probability = mutation_probability
        self.gen_n = 0
        self.same_fitness_counter = 0
        self.last_fitness = 0
        self.plot_array = {"max": [], "min": [], "avg": []}
        self.init_population()

    def init_population(self):
        for i in range(self.population_size):
            self.population[i] = Individual(len(self.possible_elements), self.mutation_probability)

    def optimize(self):
        self.start_time = time.time()
        absolute_max_weight = 0
        for el in self.possible_elements:
            absolute_max_weight += el["weight"]

        while not self.has_to_stop():
            self.gen_n += 1
            for individual in self.population:
                individual.calculate_fitness(self.possible_elements, self.max_elements,
                                             self.max_weight, absolute_max_weight)

            children = []
            while len(children) < self.population_size:
                [first_parent, second_parent] = np.random.choice(self.population, 2, replace=False)
                [first_child, second_child] = first_parent.cross(second_parent, self.crosser)
                first_child.mutate()
                first_child.calculate_fitness(self.possible_elements, self.max_elements,
                                              self.max_weight, absolute_max_weight)
                second_child.mutate()
                second_child.calculate_fitness(self.possible_elements, self.max_elements,
                                               self.max_weight,absolute_max_weight)
                children.append(first_child)
                children.append(second_child)

            for n in self.population:  # 2*size
                children.append(n)

            children = self.selector(children, self.population_size)  # , self.gen_n)
            for idx, individual in enumerate(children):
                self.population[idx] = individual

            best_fitness = max([ind.fitness for ind in self.population])
            if best_fitness == self.last_fitness:
                self.same_fitness_counter += 1
            else:
                self.same_fitness_counter = 0

            self.plot_array["max"].append(best_fitness)
            self.plot_array["min"].append(min([ind.fitness for ind in self.population]))
            self.plot_array["avg"].append(average([ind.fitness for ind in self.population]))

            self.last_fitness = best_fitness

        print("--- %s Seconds ---" % (time.time() - self.start_time))
        for individual in self.population:
            individual.calculate_fitness(self.possible_elements, self.max_elements,
                                         self.max_weight, absolute_max_weight)

        best_fitness = 0
        best_fitness_idx = -1
        for idx, ind in enumerate(self.population):
            if ind.fitness > best_fitness:
                best_fitness = ind.fitness
                best_fitness_idx = idx

        print("Optimized solution:", self.population[best_fitness_idx])
        print("Optimized solution benefit:", self.population[best_fitness_idx].gains)
        print("Optimized solution weight:", self.population[best_fitness_idx].weight)

    def get_plot_array(self):
        return self.plot_array

    def has_to_stop(self):
        return self.gen_n > 1000 or (
                self.gen_n > self.min_generations and any(ind.is_valid() for ind in self.population)
        )
