import numpy


class Tree:
    def __init__(self, initial_state):
        self.root = self.Node(initial_state, numpy.array([]), None)

    def insert(self, parent, state):
        numpy.append(parent.successors, self.Node(state, numpy.array([]), parent))

    class Node:
        def __init__(self, state, successors, parent):
            self.state = state
            self.successors = successors
            self.parent = parent
            self.cost = 0
            if parent is not None:
                self.cost = parent.get_cost + 1

        def get_successors(self):
            return self.successors

        def get_cost(self):
            return self.cost

