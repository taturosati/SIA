import json
import sys
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

    if config['algo'] == 'BPA':
        s = BFSsolver(Puzzle())
    elif config['algo'] == 'BPP':
        s = DFSsolver(Puzzle())
    elif config['algo'] == 'LOCAL':
        s = LocalHeuristicSolver(Puzzle(heu))
    elif config['algo'] == 'GLOBAL':
        s = GlobalHeuristicSolver(Puzzle(heu))
    elif config['algo'] == 'A*':
        s = AStarSolver(Puzzle(heu))
    elif config['algo'] == 'BPPV':
        if 'limit' in config:
            limit = config['limit']
        s = VDFSsolver(Puzzle(), limit)
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
