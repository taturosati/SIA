from selector import Selector
from optimizer import Optimizer
from crosser import Crosser
# if len(sys.argv) < 2 or not str(sys.argv[1]).endswith('.json'):
#     print('Please enter the configuration file (e.g. python3 main.py config.json)')
#     exit()

# with open(sys.argv[1], 'r') as config_file:
#     config = json.load(config_file)}

possible_elements = []

with open('./data.txt', 'r') as data_file:
    [max_elements, max_weight] = [int(n) for n in data_file.readline().split()]
    for line in data_file:
        [gains, weight] = [int(n) for n in line.split()]
        possible_elements.append({
            'gains': gains,
            'weight': weight
        })

print(max_elements, max_weight)

# TODO: read what selector to use from config
optimizer = Optimizer(possible_elements, 500, max_elements, max_weight, lambda population, size: Selector.truncate_select(population, size, 95), lambda first, second: Crosser.multiple_cross(first, second, 2))
optimizer.optimize()



