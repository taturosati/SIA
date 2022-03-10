import numpy as np
import hashlib


class Tree:
    def __init__(self, initial_state):
        self.root = self.Node(initial_state, np.array([]), None)
    
    def get_root(self):
        return self.root

    def insert(self, parent, state):
        to_insert = self.Node(state, np.array([]), parent)
        np.append(parent.successors, to_insert)
        return to_insert

    class Node:
        def __init__(self, state, successors, parent):
            self.state = state # This is a Puzzle
            self.successors = successors
            self.parent = parent
            self.cost = 0 # We assume that the cost is uniform so, cost = depth
            if parent is not None:
                self.cost = parent.get_cost() + 1

        def get_state(self):
            return self.state

        def get_successors(self):
            return self.successors

        def get_cost(self):
            return self.cost

        def get_parent(self):
            return self.parent

        def __key(self):
            return (self.state.get_board())

        def __hash__(self):
            return hash(hashlib.sha1(self.__key()).hexdigest())
            
        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.state == other.state
            return NotImplemented

        def __ne__(self, other):
            x = self.__eq__(other)
            if x is NotImplemented:
                return NotImplemented

            return not x

