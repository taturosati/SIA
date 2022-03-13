from solvers.solver import Solver


class LocalHeuristicSolver(Solver):
    def __init__(self, puzzle):
        super().__init__(puzzle, LocalHeuristicSolver.node_comparator)

    @staticmethod
    def node_comparator(n1, n2):
        if n1.get_cost() == n2.get_cost():
            return n1.get_state().heuristic() < n2.get_state().heuristic()

        return n1.get_cost() > n2.get_cost()
