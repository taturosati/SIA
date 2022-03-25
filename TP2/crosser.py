from individual import Individual
import numpy as np
import random


class Crosser:
    @staticmethod
    def simple_cross(first_parent, second_parent):
        size = len(first_parent.genome)  # TODO ver de recibirlo
        first_child = Individual(size, False)
        second_child = Individual(size, False)
        p = random.randint(0, size)
        for i in range(p):
            first_child.genome[i] = first_parent.genome[i]
            second_child.genome[i] = second_parent.genome[i]
        for i in range(p + 1, size):
            first_child.genome[i] = second_parent.genome[i]
            second_child.genome[i] = first_parent.genome[i]

        return [first_child, second_child]

    @staticmethod
    def multiple_cross(first_parent, second_parent, n):
        size = len(first_parent.genome)  # TODO ver de recibirlo
        first_child = Individual(size, False)
        second_child = Individual(size, False)
        p = sorted(random.sample(range(1, size), n))
        change_counter = 0

        for i in range(size):
            if change_counter < n and i == p[change_counter]:  # TODO chequear
                change_counter += 1
            if change_counter % 2 == 0:
                first_child.genome[i] = second_parent.genome[i]
                second_child.genome[i] = first_parent.genome[i]
            else:
                first_child.genome[i] = first_parent.genome[i]
                second_child.genome[i] = second_parent.genome[i]
        return [first_child, second_child]

    @staticmethod
    def uniform_cross(first_parent, second_parent):
        size = len(first_parent.genome)  # TODO ver de recibirlo
        first_child = Individual(size, False)
        second_child = Individual(size, False)

        for i in range(size):
            if np.random.uniform() > 0.5:
                first_child.genome[i] = second_parent.genome[i]
                second_child.genome[i] = first_parent.genome[i]
            else:
                first_child.genome[i] = first_parent.genome[i]
                second_child.genome[i] = second_parent.genome[i]

        return [first_child, second_child]
