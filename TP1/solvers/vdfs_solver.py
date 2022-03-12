import bisect, time
from solvers.solver import Solver


class VDFSsolver(Solver):
    def __init__(self, puzzle, limit):
        super().__init__(puzzle, VDFSsolver.node_comparator)
        self.limit = limit
        self.prev_limit = 0
        self.solution = []

    @staticmethod
    def node_comparator(n1, n2):
        return n1.get_cost() < n2.get_cost()

    def solve(self):
        start_time = time.time()
        bisect.insort(self.frontier, self.tree.get_root())
        self.vdfs_solve()
        if len(self.solution) == 0:
            Solver.print_stats(self, start_time)
        else:
            Solver.print_stats(self, start_time, self.solution[-1])
    
        return self.solution

    def vdfs_solve(self): 
        print('Trying to find solution for limit', self.limit)

        limit_list = []
        while len(self.frontier) > 0:
            curr_node = self.frontier.pop(0)
            curr_state = curr_node.get_state()
            
            if str(curr_state.get_board()) not in self.explored:
                self.explored[str(curr_state.get_board())] = curr_node  # TODO stringify de otra manera
            else: 
                self.explored[str(curr_state.get_board())] = curr_node

            if curr_state.is_solution():     
                self.solution = []
                while curr_node is not None:
                    self.solution.insert(0, curr_node)
                    curr_node = curr_node.get_parent()

                print('Found solution with cost', len(self.solution)-1)

                if len(self.solution) - 1 - self.prev_limit > 1:
                    aux = self.prev_limit
                    self.prev_limit = self.limit
                    self.limit = int((aux + len(self.solution) - 1)/2)
                    self.frontier = [n for n in self.frontier if n.get_cost() <= self.limit]
                    for n in limit_list:
                        bisect.insort(self.frontier, n)

                    return self.vdfs_solve()
                
                return self.solution

            valid_moves = self.valid_moves(curr_state)
            for move in valid_moves:
                new_puzzle = curr_state.copy()
                empty_row, empty_col = new_puzzle.get_empty_square_position()
                new_puzzle.move_square(move[0], move[1], empty_row, empty_col)
                new_node = self.tree.insert(curr_node, new_puzzle)
                if (str(new_node.get_state().get_board()) not in self.explored or \
                    new_node.get_cost() < self.explored[str(new_node.get_state().get_board())].get_cost()) and \
                    new_node.get_cost() < self.limit:
                    bisect.insort(self.frontier, new_node)
                elif new_node.get_cost() == self.limit:
                    bisect.insort(limit_list, new_node)
        
        
        if len(limit_list) == 0 and len(self.solution) == 0:
            return []
        
        if len(self.solution) > 0:
            if abs(len(self.solution) - 1 - self.limit) <= 1:
                return self.solution

            self.prev_limit = self.limit
            self.limit = int((self.prev_limit + len(self.solution) - 1)/2)
        else:
            self.prev_limit = self.limit
            self.limit += 10

        self.frontier = limit_list

        return self.vdfs_solve()
        
