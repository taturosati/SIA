from solvers.solver import Solver


class VDFSsolver(Solver):
    def __init__(self, puzzle, limit):
        super().__init__(puzzle, VDFSsolver.node_comparator)
        self.limit = limit

    @staticmethod
    def node_comparator(n1, n2):
        return n1.get_cost() < n2.get_cost()