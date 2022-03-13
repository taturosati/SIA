import math

class Heuristics():
    correct_position = {0: (2, 2), 1: (0, 0), 2: (0, 1), 3: (0, 2),
                        4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1)}

    @staticmethod
    def get_target_position(num):
        return Heuristics.correct_position[num]

    @staticmethod
    def euclidean_heuristic(board, row, col):
        target_row, target_col = Heuristics.get_target_position(board[row][col])
        return 0 if board[row][col] == 0 else math.sqrt(math.pow(row - target_row, 2) + math.pow(col - target_col, 2))
    
    @staticmethod
    def out_of_pos_heuristic(board, row, col):
        target_row, target_col = Heuristics.get_target_position(board[row][col])
        return 0 if board[row][col] == 0 or (row == target_row and col == target_col) else 1
    
    @staticmethod
    def penalized_manhattan_heuristic(board, row, col):
        target_row, target_col = Heuristics.get_target_position(board[row][col])
        other_row, other_col = Heuristics.get_target_position(board[target_row][target_col])

        if target_row == other_row and target_col == other_col: # It already is in place
            return 0

        distance = abs(target_row - row) + abs(target_col - col)
        if other_row == row and other_col == col: 
            return distance + 2 # Switched places, add penalty

        return distance
