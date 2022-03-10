import numpy as np
import bisect

from tree import Tree

class Solver:
    def __init__(self, puzzle, comparator):
        self.tree = Tree(puzzle, comparator)
        self.explored = set()
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
        bisect.insort(self.frontier, self.tree.get_root())
        while len(self.frontier) > 0:
            current = self.frontier.pop(0)
            if current not in self.explored:
                self.explored.add(current)

            if current.get_state().is_solution(current.get_state().get_board()):
                print('Solved!')
                print('Cost: ' + str(current.get_cost()))
                print('Depth: ' + str(current.get_cost()))
                self.print_stats()
                solution = []

                while(current is not None):
                    solution.insert(0, current)
                    current = current.get_parent()

                return solution
            
            valid_moves = self.valid_moves(current.get_state())
            for move in valid_moves:
                new_puzzle = current.get_state().copy()
                empty_row, empty_col = new_puzzle.get_empty_square_position()
                new_puzzle.move_square(move[0], move[1], empty_row, empty_col)
                new_node = self.tree.insert(current, new_puzzle)
                if new_node not in self.explored:
                    bisect.insort(self.frontier, new_node)

            
        print('There is no solution')
        self.print_stats()
        return []

    def print_stats(self):
        print('Frontier nodes: ' + str(len(self.frontier)))
        print('Explored nodes: ' + str(len(self.explored)))