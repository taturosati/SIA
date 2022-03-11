from solvers.solver import Solver


class AStarSolver(Solver):
    def __init__(self, puzzle):
        super().__init__(puzzle, AStarSolver.node_comparator)

    @staticmethod
    def node_comparator(n1, n2):
        return n1.get_state().heuristic() + n1.get_cost() < n2.get_state().heuristic() + n2.get_cost()
