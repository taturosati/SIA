import numpy as np
import bisect

from tree import Tree
import time


class Solver:
    def __init__(self, puzzle, comparator):
        self.tree = Tree(puzzle, comparator)
        self.explored = {}
        self.frontier = []

    def valid_moves(self, puzzle):
        row, col = puzzle.get_empty_square_position()
        valid_moves = []

        if row > 0:
            valid_moves.append([row - 1, col])
        if row < 2:
            valid_moves.append([row + 1, col])
        if col > 0:
            valid_moves.append([row, col - 1])
        if col < 2:
            valid_moves.append([row, col + 1])

        return valid_moves

    def solve(self):
        start_time = time.time()
        bisect.insort(self.frontier, self.tree.get_root())
        while len(self.frontier) > 0:
            curr_node = self.frontier.pop(0)
            curr_state = curr_node.get_state()

            if str(curr_state.get_board()) not in self.explored:
                self.explored[str(curr_state.get_board())] = curr_node # TODO stringify de otra manera

            if curr_state.is_solution():
                print("--- %s seconds ---" % (time.time() - start_time))
                print('Solved!')
                print('Cost: ' + str(curr_node.get_cost()))
                print('Depth: ' + str(curr_node.get_cost()))
                self.print_stats()
                solution = []
                while(curr_node is not None):
                    solution.insert(0, curr_node)
                    curr_node = curr_node.get_parent()
                return solution

            valid_moves = self.valid_moves(curr_state)
            for move in valid_moves:
                new_puzzle = curr_state.copy()
                empty_row, empty_col = new_puzzle.get_empty_square_position()
                new_puzzle.move_square(move[0], move[1], empty_row, empty_col)
                new_node = self.tree.insert(curr_node, new_puzzle)
                if str(new_node.get_state().get_board()) not in self.explored:
                    bisect.insort(self.frontier, new_node)

        print("--- %s seconds ---" % (time.time() - start_time))
        print('There is no solution')
        self.print_stats()
        return []

    def print_stats(self):
        print('Frontier nodes: ' + str(len(self.frontier)))
        print('Explored nodes: ' + str(len(self.explored)))
