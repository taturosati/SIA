import numpy
import numpy as np


class Puzzle:
    objective = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def __init__(self):
        # self.board = np.array(np.random.choice(9, size=(3, 3), replace=False))
        self.board = np.array([[0, 3, 4], [5, 7, 6], [1, 2, 8]])
        self.empty_square = self.find_empty()  # TODO primero hacemos un find en realidad

    @staticmethod
    def valid_position(row, col):
        return 0 <= row <= 2 and 0 <= col <= 2

    def print_board(self):
        print()
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end='')
            print()

    def move_square(self, from_row, from_col, to_row, to_col):
        # TODO modularizar
        if not Puzzle.valid_position(from_row, from_col) or not Puzzle.valid_position(to_row, to_col) or \
                self.board[to_row][to_col] != 0 or (abs(from_row - to_row) + abs(from_col - to_col)) != 1:
            return False

        self.board[to_row][to_col], self.board[from_row][from_col] = self.board[from_row][from_col], 0
        self.empty_square = (from_row, from_col)

    def valid_moves(self):
        row, col = self.empty_square[0], self.empty_square[1]
        valid_moves = np.array([])

        if row > 0:
            numpy.append(valid_moves, (row - 1, col))
        if row < 3:
            numpy.append(valid_moves, (row + 1, col))
        if col > 0:
            numpy.append(valid_moves, (row, col - 1))
        if col < 3:
            numpy.append(valid_moves, (row, col + 1))

        return valid_moves

    def is_solution(self):
        return np.array_equal(self.board, self.objective)

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def get_state(self):
        return self.board

    def get_empty_square_position(self):
        return self.empty_square

