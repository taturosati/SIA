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
        gen: int
        # selector,
        # crosser,
    ):
        self.possible_elements = possible_elements
        self.population = np.empty(population_size, Individual)
        self.population_size = population_size
        self.max_elements = max_elements
        self.max_weight = max_weight
        self.selector = lambda population, size: Selector.direct_select(
            population, size
        )
        self.crosser = lambda first, second: Crosser.simple_cross(first, second)
        self.gen = gen
        self.generations = 0
        self.init_population()

    def set_crosser(self, crosser: Crosser):
        self.crosser = crosser

    def set_selector(self, selector: Selector):
        self.selector = selector

    def init_population(self):
        for i in range(self.population_size):
            self.population[i] = Individual(len(self.possible_elements))
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


class OptimizerBuilder:
    def __init__(
        self,
        possible_elements: array,
        population_size: int,
        max_elements: int,
        max_weight: int,
        gen=500,
    ):
        self.optimizer = Optimizer(
            possible_elements, population_size, max_elements, max_weight, gen
        )

    def build(self):
        return self.optimizer

    def with_corsser(self, crosser: str, n=1):
        if crosser == "simple":
            print("simple")
            # self.optimizer.setCrosser(
            #     lambda first, second: Crosser.simple_cross(first, second)
            # )
            pass
        elif crosser == "multiple":
            print("multiple")
            self.optimizer.set_crosser(
                lambda first, second: Crosser.multiple_cross(first, second, n)
            )
        elif crosser == "uniform":
            print("uniform")
            self.optimizer.set_crosser(
                lambda first, second: Crosser.uniform_cross(first, second)
            )
        else:
            raise "Invalid cross method"

        return self

    def with_selector(self, selector: str, u=0.6, t0=80000, tf=60000, k=1, trunc=10):
        if selector == "direct":
            print("direct")
            # self.optimizer.setSelector(
            #     lambda population, size: Selector.direct_select(population, size)
            # )
            pass
        elif selector == "roulette":
            print("roulette")
            self.optimizer.set_selector(
                lambda population, size: Selector.roulette_select(population, size)
            )
        elif selector == "rank":
            print("rank")
            self.optimizer.set_selector(
                lambda population, size: Selector.rank_select(population, size)
            )
        elif selector == "tournament":
            print("tournament")
            self.optimizer.set_selector(
                lambda population, size: Selector.tournament_select(population, size, u)
            )
        elif selector == "boltzman":
            print("boltzman")
            self.optimizer.set_selector(
                lambda population, size, generation: Selector.boltzman_select(
                    population, size, generation, t0, tf, k
                )
            )
        elif selector == "truncate":
            print("truncate")
            self.optimizer.set_selector(
                lambda population, size: Selector.truncate_select(
                    population, size, trunc
                )
            )
        else:
            raise "Invalid selector method"

        return self
