import numpy as np
from plotter import plot
from configurer import Configurer
from selector import Selector
from optimizer import Optimizer
import sys

if len(sys.argv) == 1 or not str(sys.argv[1]).endswith(".json"):
    print("Please enter the configuration file (e.g. python3 main.py config.json)")
    exit()

# with open(sys.argv[1], "r") as config_file:
#     config = json.load(config_file)

possible_elements = []
with open("./data.txt", "r") as data_file:
    [max_elements, max_weight] = [int(n) for n in data_file.readline().split()]
    for line in data_file:
        [gains, weight] = [int(n) for n in line.split()]
        possible_elements.append({"gains": gains, "weight": weight})
    data_file.close()

configuration = Configurer.configure(sys.argv[1], len(possible_elements))

# print(max_elements, max_weight)
# print("configuration: ", gen, p, o, a, cross, selection)

optimizer = Optimizer(
    possible_elements,
    500,
    max_elements,
    max_weight,
    configuration["gen"],
    configuration["selector"],
    configuration["crosser"],
    configuration["p"],
)
optimizer.optimize()
plot(optimizer.get_plot_array(), "Truncate - n = 65 - uniform")
