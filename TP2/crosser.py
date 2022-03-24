from individual import Individual
import numpy as np
import random

class Crosser:
    @staticmethod
    def simple_cross(first, second):
        first_child = Individual(len(first.genome))
        second_child = Individual(len(second.genome))
        p = random.randint(0, len(first.genome))
        for i in range(p):
            first_child.genome[i] = first.genome[i]
            second_child.genome[i] = second.genome[i]

        for i in range(p+1, len(first.genome)):
            first_child.genome[i] = second.genome[i]
            second_child.genome[i] = first.genome[i]

        return [first_child, second_child]
    
    @staticmethod
    def multiple_cross(first, second, n):
        first_child = Individual(len(first.genome))
        second_child = Individual(len(second.genome))
        p = sorted(random.sample(range(1, len(first.genome)), n))
        change_counter = 0

        for i in range(len(first.genome)):
            if change_counter < n and i == p[change_counter]: change_counter += 1
            if change_counter % 2 == 0:
                first_child.genome[i] = second.genome[i]
                second_child.genome[i] = first.genome[i]
            else:
                first_child.genome[i] = first.genome[i]
                second_child.genome[i] = second.genome[i] 
        return [first_child, second_child]

    @staticmethod
    def uniform_cross(first, second):
        first_child = Individual(len(first.genome))
        second_child = Individual(len(second.genome))

        for i in range(len(first.genome)):
            if np.random.uniform() > 0.5:
                first_child.genome[i] = second.genome[i]
                second_child.genome[i] = first.genome[i]
            else:
                first_child.genome[i] = first.genome[i]
                second_child.genome[i] = second.genome[i]

        return [first_child, second_child]
    

