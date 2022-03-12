import numpy as np
import math


class Puzzle:
    objective = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    correct_position = {0: (2, 2), 1: (0, 0), 2: (0, 1), 3: (0, 2),
                        4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1)}

    def __init__(self, heuristic_config='EUC'):
        self.board = np.array(np.random.choice(9, size=(3, 3), replace=False))  # Random
        #self.board = np.array([[8, 1, 2], [0, 4, 3], [7, 6, 5]])  # No solution
        #self.board = np.array([[8, 6, 7], [2, 5, 4], [3, 0, 1]])   # Hardest solution
        #self.board = np.array([[3, 1, 8], [5, 6, 7], [0, 4, 2]])  # Has solution
        self.empty_square = self.find_empty()
        self.heuristic_config = heuristic_config

    def heuristic(self):
        to_return = 0
        for (i, row) in enumerate(self.board):
            for (j, square) in enumerate(row):
                target = self.correct_position[square]
                if self.heuristic_config == 'EUC':
                    to_return += math.sqrt(math.pow(i - target[0], 2) + math.pow(j - target[1], 2))
                else:
                    to_return += abs(i - target[0]) + abs(j - target[1])

        return to_return

    @staticmethod
    def valid_position(row, col):
        return 0 <= row <= 2 and 0 <= col <= 2

    def copy(self):
        puzzle = Puzzle()
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
                # print(self.board[i][j], end='')
            to_return += '\n'
            # print()
        to_return += '\n'
        return to_return

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        return Puzzle.valid_position(from_row, from_col) and Puzzle.valid_position(to_row, to_col) and \
               self.board[to_row][to_col] == 0 and (
                       abs(from_row - to_row) + abs(from_col - to_col)) == 1

    def move_square(self, from_row, from_col, to_row, to_col):
        if not self.is_valid_move(from_row, from_col, to_row, to_col):
            return False

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
