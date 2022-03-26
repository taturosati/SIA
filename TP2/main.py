from selector import Selector
from optimizer import Optimizer, OptimizerBuilder
from crosser import Crosser
import sys
import json

if len(sys.argv) == 1 or not str(sys.argv[1]).endswith(".json"):
    print("Please enter the configuration file (e.g. python3 main.py config.json)")
    exit()

with open(sys.argv[1], "r") as config_file:
    config = json.load(config_file)

    ## TODO: pasar todo a un archivo de configuración
    gen = 500
    if "gen" in config and config["gen"] >= 500:
        gen = config["gen"]
    # else:
    #     print("Amount of generations must be grater than 500")
    #     config_file.close()
    #     exit()

    p = 0.01
    if "p" in config and 0 < config["p"] <= 1:
        p = config["p"]
    # else:
    #     print("p € U[0,1]")
    #     config_file.close()
    #     exit()
    a = 0.01
    if "a" in config and 0 < config["a"] <= 1:
        a = config["a"]
    # else:
    #     print("a € U[0.5,1]")
    #     config_file.close()
    #     exit()
    o = 0.01
    if "o" in config and 0 < config["o"] <= 1:
        o = config["o"]
    # else:
    #     print("o € U[0.5,1]")
    #     config_file.close()
    #     exit()
    t0 = 80000
    if "t0" in config and 0 < config["t0"]:
        t0 = config["t0"]
    # else:
    #     print("0 < t0")
    #     config_file.close()
    #     exit()
    tf = 60000
    if "tf" in config and 0 < config["tf"] < t0:
        tf = config["tf"]
    # else:
    #     print("0 < tf < t0")
    #     config_file.close()
    #     exit()
    if "k" in config and 0 < config["k"] <= 1:
        k = config["k"]
    # else:
    #     print("0 < k <= 1")
    #     config_file.close()
    #     exit()

    selection = "direct"
    if "selection" in config:
        #     if (
        #         config["selection"] == "elite"
        #         or config["selection"] == "roulette"
        #         or config["selection"] == "rank"
        #         or config["selection"] == "tournament"
        #         or config["selection"] == "boltzman"
        #         or config["selection"] == "truncate"
        #     ):
        selection = config["selection"]
    # else:
    #     print("Wrong selection algorithm")
    #     config_file.close()
    #     exit()

    cross = "simple"
    if "cross" in config:
        #     if (
        #         config["cross"] == "simple"
        #         or config["cross"] == "multiple"
        #         or config["cross"] == "uniform"
        #     ):
        cross = config["cross"]
    # else:
    #     print("Wrong cross algorithm")
    #     config_file.close()
    #     exit()

possible_elements = []
with open("./data.txt", "r") as data_file:
    [max_elements, max_weight] = [int(n) for n in data_file.readline().split()]
    for line in data_file:
        [gains, weight] = [int(n) for n in line.split()]
        possible_elements.append({"gains": gains, "weight": weight})
    data_file.close()

print(max_elements, max_weight)
# print("configuration: ", gen, p, o, a, cross, selection)

# TODO: read what selector to use from config
# optimizer = Optimizer(
#     possible_elements,
#     500,
#     max_elements,
#     max_weight,
#     lambda population, size, generation: Selector.boltzman_select(
#         population, size, generation, 80000, 60000, 1
#     ),
#     lambda first, second: Crosser.multiple_cross(first, second, 2),
# )

optimizer = (
    OptimizerBuilder(possible_elements, 500, max_elements, max_weight, gen)
    .with_corsser(cross)
    .with_selector(selection)
    .build()
)
optimizer.optimize()
config_file.close()
