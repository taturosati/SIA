import json
import sys
import numpy
from solvers.dfs_solver import DFSsolver
from solvers.bfs_solver import BFSsolver
from solvers.vdfs_solver import VDFSsolver
from solvers.global_heuristic_solver import GlobalHeuristicSolver
from solvers.local_heuristic_solver import LocalHeuristicSolver
from solvers.a_star_solver import AStarSolver

from puzzle import Puzzle

if len(sys.argv) < 2 or not str(sys.argv[1]).endswith('.json'):
    print('Please enter the configuration file (e.g. python3 main.py config.json)')
    exit()

with open(sys.argv[1], 'r') as config_file:
    config = json.load(config_file)

    if not 'algo' in config:
        print('Must specify algorithm in config file')
        config_file.close()
        exit()

    heu = 'EUC'
    if 'heu' in config:
        heu = config['heu']

    limit = 20
    if 'limit' in config:
        limit = config['limit']

    init_state = None
    if 'initial_state' in config:
        init_state_array = [int(x) for x in config['initial_state']]
        init_state = numpy.array([
            [init_state_array[0], init_state_array[1], init_state_array[2]],
            [init_state_array[3], init_state_array[4], init_state_array[5]],
            [init_state_array[6], init_state_array[7], init_state_array[8]]
        ])

    if config['algo'] == 'BPA':
        s = BFSsolver(Puzzle(init_state))
    elif config['algo'] == 'BPP':
        s = DFSsolver(Puzzle(init_state))
    elif config['algo'] == 'LOCAL':
        s = LocalHeuristicSolver(Puzzle(init_state, heu))
    elif config['algo'] == 'GLOBAL':
        s = GlobalHeuristicSolver(Puzzle(init_state, heu))
    elif config['algo'] == 'A*':
        s = AStarSolver(Puzzle(init_state, heu))
    elif config['algo'] == 'BPPV':
        s = VDFSsolver(Puzzle(init_state), limit)
    else:
        print('Wrong algorithm inserted')
        config_file.close()
        exit()
    config_file.close()

solution = s.solve()

if len(solution) > 0:
    with open('solution.txt', 'w') as solution_file:
        for node in solution:
            solution_file.write(node.get_state().string_board())
        solution_file.close()
