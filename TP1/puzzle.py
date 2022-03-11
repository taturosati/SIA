import numpy as np


class Puzzle:
    objective = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def __init__(self):
        self.board = np.array(np.random.choice(
            9, size=(3, 3), replace=False))  # Random
        # self.board = np.array([[8, 1, 2], [0, 4, 3], [7, 6, 5]]) # No solution
        # self.board = np.array(
        #     [[0, 1, 2], [3, 4, 5], [6, 7, 8]])  # Has solution
        # TODO primero hacemos un find en realidad
        self.empty_square = self.find_empty()

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
                to_return = to_return + str(self.board[i][j])
                # print(self.board[i][j], end='')
            to_return = to_return + '\n'
            # print()
        to_return = to_return + '\n'
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

    def is_solution(self, board):
        return np.array_equal(board, Puzzle.objective)

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
