import json
import sys
from solvers.dfs_solver import DFSsolver
from solvers.bfs_solver import BFSsolver

from puzzle import Puzzle

# config = {"algo": "BPA"}
if len(sys.argv) != 2 or not str(sys.argv[1]).endswith('.json'):
    print('Please enter the configuration file (e.g. python3 main.py config.json)')
    exit()

# print(str(sys.argv))

with open(sys.argv[1], 'r') as config_file:
    config = json.load(config_file)

    if not 'algo' in config:
        print('Must specify algorithm in config file')
        config_file.close()
        exit()

    if config['algo'] == 'BPA':
        s = BFSsolver(Puzzle())
    elif config['algo'] == 'BPP':
        s = DFSsolver(Puzzle())
    elif config['algo'] == 'BPPV':
        s = BFSsolver(Puzzle())
    else:
        print('Wrong algorythm inserted')
        config_file.close()
        exit()

    config_file.close()


# p = Puzzle()
# p.print_board()
# p.move_square(0, 1, 0, 0)
# print(p.is_solution())
# p.print_board()
# p.move_square(1, 1, 0, 1)
# p.print_board()

# s = DFSsolver(Puzzle())
solution = s.solve()

if len(solution) > 0:
    with open('solution.txt', 'w') as solution_file:
        for node in solution:
            solution_file.write(node.get_state().string_board())
        solution_file.close()
