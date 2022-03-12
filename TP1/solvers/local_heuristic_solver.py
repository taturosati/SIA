from solvers.solver import Solver


class LocalHeuristicSolver(Solver):
    def __init__(self, puzzle):
        super().__init__(puzzle, LocalHeuristicSolver.node_comparator)

    @staticmethod
    def node_comparator(n1, n2):  # TODO chequear
        if n1.get_cost() == n2.get_cost():
            return n1.get_state().heuristic() < n2.get_state().heuristic()

        return n1.get_cost() > n2.get_cost()
        # tambien se puede con tuplas, lo podemos probar despues aunque el costo tiene que estar al reves
        # (n2.cost, n1.heu) < (n1.cost, n2.heu)
