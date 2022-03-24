import json
import sys
import numpy
from solvers.dfs_solver import DFSsolver
from solvers.bfs_solver import BFSsolver
from solvers.vdfs_solver import VDFSsolver
from solvers.global_heuristic_solver import GlobalHeuristicSolver
from solvers.local_heuristic_solver import LocalHeuristicSolver
from solvers.a_star_solver import AStarSolver

from models.puzzle import Puzzle

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
        if config['heu'] != 'EUC' or config['heu'] != 'MAN' or config['heu'] != 'OOP':
            heu = config['heu']
        else:
            print('Wrong algorithm')
            config_file.close()
            exit()

    limit = 20
    if 'limit' in config:
        if config['limit'] > 0:
            limit = config['limit']
        else:
            print('Wrong limit')
            config_file.close()
            exit()

    init_state = None
    if 'initial_state' in config:
        if len(config['initial_state']) == 9 and config['initial_state'].isnumeric():
            init_state_array = [int(x) for x in config['initial_state']]
            init_state = numpy.array([
                init_state_array[0:3],
                init_state_array[3:6],
                init_state_array[6:9]
            ])
        else:
            print('Wrong configuration')
            config_file.close()
            exit()

    algo = config['algo']
    heuristics = {"MAN": "Manhattan", "EUC": "Euclidean", "OOP": "Out of Position"}

    if algo == 'BPA':
        s = BFSsolver(Puzzle(init_state))
    elif algo == 'BPP':
        s = DFSsolver(Puzzle(init_state))
    elif algo == 'BPPV':
        print("Limit:", limit)
        s = VDFSsolver(Puzzle(init_state), limit)
    elif algo == 'LOCAL':
        print("Heuristic:", heuristics[heu])
        s = LocalHeuristicSolver(Puzzle(init_state, heu))
    elif algo == 'GLOBAL':
        print("Heuristic:", heuristics[heu])
        s = GlobalHeuristicSolver(Puzzle(init_state, heu))
    elif algo == 'A*':
        print("Heuristic:", heuristics[heu])
        s = AStarSolver(Puzzle(init_state, heu))
    else:
        print('Wrong algorithm inserted')
        config_file.close()
        exit()
    config_file.close()

print("Alorithm:", algo)

solution = s.solve()

if len(solution) > 0:
    with open('solution.txt', 'w') as solution_file:
        for node in solution:
            solution_file.write(node.get_state().string_board())
        solution_file.close()
