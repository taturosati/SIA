from mimetypes import init
from models.heuristics import Heuristics
import numpy as np

class Puzzle:
    objective = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    correct_position = {0: (2, 2), 1: (0, 0), 2: (0, 1), 3: (0, 2),
                        4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1)}
    

    def __init__(self, initial_state, heuristic_config='EUC'):
        if initial_state is None:
            self.board = np.array(np.random.choice(
                9, size=(3, 3), replace=False))  # Random
        else:
            self.board = initial_state
        self.empty_square = self.find_empty()
        self.heuristic_config = heuristic_config


    def heuristic(self):
        to_return = 0
        for row in range(3):
            for col in range(3):
                if self.heuristic_config == 'EUC':
                    to_return += Heuristics.euclidean_heuristic(self.board, row, col)
                elif self.heuristic_config == 'OOP':
                    to_return += Heuristics.out_of_pos_heuristic(self.board, row, col)
                else:
                    to_return += Heuristics.penalized_manhattan_heuristic(self.board, row, col)

        return to_return

    @staticmethod
    def valid_position(row, col):
        return 0 <= row <= 2 and 0 <= col <= 2

    def copy(self):
        puzzle = Puzzle(self.board, self.heuristic_config)
        puzzle.board = self.board.copy()
        puzzle.empty_square = self.empty_square
        return puzzle

    def print_board(self):
        print()
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end='')
            print()

    def string_board(self):
        to_return = ''
        for i in range(3):
            for j in range(3):
                to_return += str(self.board[i][j])
            to_return += '\n'
        to_return += '\n'
        return to_return

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        return Puzzle.valid_position(from_row, from_col) and Puzzle.valid_position(to_row, to_col) and \
            self.board[to_row][to_col] == 0 and (
            abs(from_row - to_row) + abs(from_col - to_col)) == 1

    def move_square(self, from_row, from_col, to_row, to_col):
        if not self.is_valid_move(from_row, from_col, to_row, to_col):
            raise 'Invalid move'

        self.board[to_row][to_col], self.board[from_row][from_col] = self.board[from_row][from_col], 0
        self.empty_square = (from_row, from_col)

    def is_solution(self):
        return np.array_equal(self.board, Puzzle.objective)

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def get_board(self):
        return self.board

    def get_empty_square_position(self):
        return self.empty_square

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return np.array_equal(self.board, other.board)
        return NotImplemented

    def __ne__(self, other):
        x = self.__eq__(other)
        if x is NotImplemented:
            return NotImplemented
        return not x

    def __str__(self):
        return ''.join([''.join([str(el) for el in row]) for row in self.board]) 

    def __key(self):
        return str(self)

    def __hash__(self):
        return hash(self.__key())     
        
