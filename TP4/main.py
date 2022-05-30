import json
import sys
from exercise_1_b import exercise_1_b
from excercise_1_a import exercise_1_a
from exercise_2 import exercise_2

if len(sys.argv) == 1 or not str(sys.argv[1]).endswith(".json"):
    print("Please enter the configuration file (e.g. python3 main.py config.json)")
    exit()


with open(sys.argv[1], "r") as config_file:
    config = json.load(config_file)
    params = {'exercise': 1, 'item': 'a', 'eta': 0.0001, 'limit': 50000, 'grid_k': 4, 'spurius_noise': 0.3, 'noise': 0.05, 'radius': 2}
    if "exercise" in config and 1 <= int(config["exercise"]) <= 2:
        params["exercise"] = int(config["exercise"])
    
    if "item" in config and len(config["item"]) == 1:
        params["item"] = config["item"]    

    if params["exercise"] == 1:
        if params["item"] == 'a':
            if "eta" in config and 0 < float(config["eta"]) <= 0.5:
                params["eta"] = float(config["eta"])
                
            if "grid_k" in config and 1 <= int(config["grid_k"]):
                params["grid_k"] = int(config["grid_k"])

            if "radius" in config and 0 < float(config["radius"]):
                params["radius"] = float(config["radius"])
                
            exercise_1_a(params)
        else:
            if "eta" in config and 0 < float(config["eta"]) <= 0.5:
                params["eta"] = float(config["eta"])
            if "limit" in config and 1 <= int(config["limit"]):
                params["limit"] = int(config["limit"])

            exercise_1_b(params)
    else:
        if "noise" in config and 0 < int(config["noise"]) < 0.5:
            params["noise"] = int(config["noise"])
        
        if "spurius_noise" in config and 0 < int(config["spurius_noise"]) < 0.5:
            params["spurius_noise"] = int(config["spurius_noise"])

        exercise_2(params)
