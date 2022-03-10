import numpy as np
from tree import Tree
from puzzle import Puzzle

class Solver:
    def __init__(self, puzzle):
        self.tree = Tree(puzzle)
        self.explored = set()
        self.frontier = set()
    
    def valid_moves(self, puzzle):
        row, col = puzzle.get_empty_square_position()
        valid_moves = []

        if row > 0:
            valid_moves.append([row - 1, col])
            # valid_moves = np.append(valid_moves, np.array([row - 1, col]))
        if row < 2:
            valid_moves.append([row + 1, col])
            # valid_moves = np.append(valid_moves, np.array([row + 1, col]))
        if col > 0:
            valid_moves.append([row, col - 1])
            # valid_moves = np.append(valid_moves, np.array([row, col - 1]))
        if col < 2:
            valid_moves.append([row, col + 1])
            # valid_moves = np.append(valid_moves, np.array([row, col + 1]))

        return valid_moves
    
    def solve(self):
        self.frontier.add(self.tree.get_root())
        last = None
        while len(self.frontier) > 0:
            current = self.frontier.pop()
            last = current.get_state()
            if current not in self.explored:
                self.explored.add(current)

            if current.get_state().is_solution(current.get_state().get_board()):
                print("solved!")
                current.get_state().print_board()
                solution = []

                while(current is not None):
                    solution.append(current)
                    current = current.get_parent()
                return solution.reverse()
            
            valid_moves = self.valid_moves(current.get_state())
            # print(len(valid_moves))
            for move in valid_moves:
                new_puzzle = current.get_state().copy()
                empty_row, empty_col = new_puzzle.get_empty_square_position()
                new_puzzle.move_square(move[0], move[1], empty_row, empty_col)
                new_node = self.tree.insert(current, new_puzzle)
                if new_node not in self.explored:
                    self.frontier.add(new_node)

            # self.frontier = set(sorted(self.frontier, key = lambda el: el.get_cost()))
            # TODO: ver si usar set o dictionary
        last.print_board()
        print("no hay solucion")
            