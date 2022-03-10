from solvers.solver import Solver


class DFSsolver(Solver):
    def __init__(self, puzzle):
        super().__init__(puzzle, DFSsolver.node_comparator)

    @staticmethod
    def node_comparator(n1, n2):
        return n1.get_cost() > n2.get_cost()
