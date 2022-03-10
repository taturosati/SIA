import json
import sys
from solver import Solver

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
    exit();

if config['algo'] == 'BPA':
    print('BPA')
elif config['algo'] == 'BPP':
    print('BPP')
elif config['algo'] == 'BPPV':
    print('BPPV')
else:
    print('Wrong algorythm inserted')
    exit()

# p = Puzzle()
# p.print_board()
# p.move_square(0, 1, 0, 0)
# print(p.is_solution())
# p.print_board()
# p.move_square(1, 1, 0, 1)
# p.print_board()

s = Solver(Puzzle())
solution = s.solve()

for i in solution:
    i.get_state().print_board()