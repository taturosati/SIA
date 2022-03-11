import bisect
import gc
from solvers.solver import Solver
# import time


class LocalHeuristicSolver(Solver):
    def __init__(self, puzzle):
        super().__init__(puzzle, LocalHeuristicSolver.node_comparator)

    def solve(self):
        node_list = []
        bisect.insort(node_list, self.tree.get_root())
        solution = []
        self.solve_rec(node_list, solution)
        return solution
        # self.solve_rec(node_list, solution)

    def solve_rec(self, node_list, solution):
        while len(node_list) > 0:
            new_list = []
            curr_node = node_list.pop(0)
            curr_state = curr_node.get_state()
            if str(curr_state.get_board()) not in self.explored:
                self.explored[str(curr_state.get_board())] = curr_node

            if curr_state.is_solution():
                # print("--- %s seconds ---" % (time.time() - start_time))
                print('Solved!')
                print('Cost: ' + str(curr_node.get_cost()))
                print('Depth: ' + str(curr_node.get_cost()))
                self.print_stats()
                while(curr_node is not None):
                    solution.insert(0, curr_node)
                    curr_node = curr_node.get_parent()
                return

            for move in self.valid_moves(curr_state):
                new_puzzle = curr_state.copy()
                empty_row, empty_col = new_puzzle.get_empty_square_position()
                new_puzzle.move_square(move[0], move[1], empty_row, empty_col)
                new_node = self.tree.insert(curr_node, new_puzzle)
                if str(new_node.get_state().get_board()) not in self.explored:
                    bisect.insort(new_list, new_node)
            
            self.solve_rec(new_list, solution)
            if len(solution) > 0:
                return


    @staticmethod
    def node_comparator(n1, n2):
        return n1.get_state().heuristic() < n2.get_state().heuristic()
