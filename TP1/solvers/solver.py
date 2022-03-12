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
        print("Solving for puzzle:")
        self.tree.get_root().get_state().print_board()
        print()
        if not self.is_solvable(self.tree.get_root().get_state().get_board()):
            print("--- %s Seconds ---" % (time.time() - start_time))
            print("There is no POSSIBLE solution for this initial configuration")
            return []

        bisect.insort(self.frontier, self.tree.get_root())
        while len(self.frontier) > 0:
            curr_node = self.frontier.pop(0)
            curr_state = curr_node.get_state()

            if str(curr_state.get_board()) not in self.explored:
                # TODO stringify de otra manera
                self.explored[str(curr_state.get_board())] = curr_node

            if curr_state.is_solution():
                self.print_stats(start_time, curr_node)
                solution = []
                while curr_node is not None:
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

        self.print_stats(start_time)
        return []

    def print_stats(self, start_time, node=None):
        print("--- %s Seconds ---" % (time.time() - start_time))
        if node is None:
            print('There is no solution')
        else:
            print('Solved!')
            print('Cost: ' + str(node.get_cost()))
            print('Depth: ' + str(node.get_cost()))
        print('Frontier nodes: ' + str(len(self.frontier)))
        print('Explored nodes: ' + str(len(self.explored)))

    # source: https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
    # A utility function to count
    # inversions in given array 'arr[]'

    @staticmethod
    def get_inv_count(arr):
        inv_count = 0
        empty_value = 0
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count

    # This function returns true
    # if given 8 puzzle is solvable.

    def is_solvable(self, puzzle):
        # Count inversions in given 8 puzzle
        inv_count = self.get_inv_count([j for sub in puzzle for j in sub])
        # return true if inversion count is even.
        return inv_count % 2 == 0

    # This code is contributed by vitorhugooli
    # Fala meu povo desse Brasil varonil
