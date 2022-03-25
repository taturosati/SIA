import math
from random import random
import numpy as np


class Selector: 
    @staticmethod
    def direct_select(population, size):
        population = sorted(population, key=lambda x: x.fitness, reverse=True)
        return population[0:size]

    @staticmethod
    def roulette_select(population, size):
        total_fitness = 0
        probabilities = []
        new_generation = []
        for individual in population:
            total_fitness += individual.fitness

        for individual in population:
            probabilities.append(individual.fitness / total_fitness)

        for _ in range(size):
            r = np.random.uniform()
            range_begin = 0
            insert = -1
            for idx, prob in enumerate(probabilities):
                if range_begin <= r <= range_begin + prob:
                    insert = idx
                    break

                range_begin += prob
            new_generation.append(population[insert])

        return new_generation

    @staticmethod
    def rank_select(population, size):
        new_generation = []
        f = lambda elem: -elem.fitness
        temp = np.argsort([f(ind) for ind in population])
        print([-f(ind) for ind in population[0:5]])
        print([-f(ind) for ind in population[0:5]])
        ranks = np.empty_like(temp)
        ranks[temp] = np.arange(len(temp))
        print(ranks[0:5])

        print("---------------")
        probabilities = []
        for i in range(len(population)):
            probabilities.append((size * 2 - ranks[i]) / (size * 2))

        for _ in range(size):
            r = np.random.uniform()
            range_begin = 0
            insert = -1
            for idx, prob in enumerate(probabilities):
                if range_begin <= r <= range_begin + prob:
                    insert = idx
                    break
                range_begin += prob

            new_generation.append(population[insert])
        return new_generation

    ## BEGIN TOURNAMENT SELECT

    @staticmethod
    def tournament_select(population, size: int, u):
        return [Selector.get_tournament_winner(population, u) for _ in range(size)]

    @staticmethod
    def get_tournament_winner(population, u):
        winners = [
            Selector.get_winner(Selector.get_pair(population), u),
            Selector.get_winner(Selector.get_pair(population), u),
        ]
        return Selector.get_winner(winners, u)

    @staticmethod
    def get_pair(population):
        return np.random.choice(population, 2, replace=False)

    @staticmethod
    def get_winner(pair, u):
        pair = sorted(pair, key=lambda x: x.fitness)
        r = np.random.uniform()
        return pair[1] if r < u else pair[0]

    ## END TOURNAMENT SELECT

    @staticmethod
    def boltzman_select(
        population, size: int, generation: int, inital_temp, target_temp, k
    ):
        temp = target_temp + (inital_temp - target_temp) * (math.e ** (-k * generation))
        total_fitness = 0

        for individual in population:
            individual.fitness = math.e ** (individual.fitness / temp)
            total_fitness += individual.fitness

        for individual in population:
            individual.fitness = individual.fitness / total_fitness

        return Selector.roulette_select(population, size)

    @staticmethod
    def truncate_select(
        population, size, k
    ):  #TODO: ese k habria que verificar que es menor a n?
        population = sorted(population, key=lambda x: x.fitness, reverse=True)[
            : len(population) + 1 - k
        ]
        return np.random.choice(population, size, replace=True)
