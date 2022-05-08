from operator import xor
import sys
import json
from first_excer import first_excercise
from second_excer import second_excercise
from third_excer import third_excercise
from utils import Utils

if len(sys.argv) == 1 or not str(sys.argv[1]).endswith(".json"):
    print("Please enter the configuration file (e.g. python3 main.py config.json)")
    exit()

exercises = [first_excercise, second_excercise, third_excercise]

with open(sys.argv[1], "r") as config_file:
        config = json.load(config_file)

        params = {'item': "a",'beta': 0.6, 'eta': 0.01, 'limit': 10000, 'k': 10, 'error_bound': 0.01}
        if "beta" in config:
            params["beta"] = float(config["beta"])
            Utils.set_beta(params["beta"])

        if "eta" in config:
            params["eta"] = float(config["eta"])

        if "limit" in config:
            params["limit"] = int(config["limit"])

        excer = 1
        if "excer" in config and 1 <= int(config["excer"]) <=3:
            excer = int(config["excer"])
        print("Excercice:", excer)

        if "item" in config:
            params["item"] = config["item"]
        print("Item:", params["item"])

        if excer == 1:
            first_excercise(params)
        elif excer == 2:
            second_excercise(params)
        else:
            if "error_bound" in config:
                params["error_bound"] = float(config["error_bound"])
            third_excercise(params)

config_file.close()