class Puzzle:
    def __init__(self):
        self.board = [[0, 3, 4], [5, 7, 6], [1, 2, 8]]

    @staticmethod
    def valid_position(row, col):
        return 0 <= row <= 2 and 0 <= col <= 2

    def print_board(self):
        print(self.board)

    def move_square(self, from_row, from_col, to_row, to_col):
        if not Puzzle.valid_position(from_row, from_col) or not Puzzle.valid_position(to_row, to_col) or \
                self.board[to_row][to_col] != 0 or (abs(from_row - to_row) + abs(from_col - to_col)) != 1:
            return False

        self.board[to_row][to_col], self.board[from_row][from_col] = self.board[from_row][from_col], 0
