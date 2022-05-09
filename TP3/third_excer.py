from plotter import plot_all_errors, plot_all_metrics
from utils import Utils
from multilayer import Multilayer
from plotter import plot_error, plot_metric
import numpy as np

def third_excercise(params: dict):
    if params["item"] == "a":
        or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
        or_out_set = [[1], [1], [-1], [-1]]
        training_set = {"in": or_in_set, "out":or_out_set}
        test_set = {"in": [], "out":[]}
        print("Solving for XOR")

        errors, metrics = Multilayer([2, 1], 2, params["eta"]).solve(training_set, test_set, params["error_bound"])
        print(min(errors))
        plot_error(errors)
    else:
        in_set = []
        with open("./number_set.txt", "r") as training_file:
                readlines = training_file.readlines()
                for idx in range(int(len(readlines) / 7)):
                    line_range = readlines[idx * 7 : (idx + 1) * 7]
                    num_array = [-1]
                    for line in line_range:
                        num_array +=  [int(n) for n in line.split()]
                    in_set.append(num_array)
                training_file.close()

        if params["item"] == "b":
            # EJERCICIO 2: PAR O IMPAR

            print("Solving number classification")
            out_set = [[1], [-1]] * 5

            in_set, out_set = Utils.shuffle_two_arrays(in_set, out_set)

            k = params["k"]
            in_parts = np.array_split(in_set, k)
            out_parts = np.array_split(out_set, k)

            all_errors = []
            all_metrics = []

            if params["validation"] == True:
                for i in range(k):
                    training_set_in = []
                    training_set_out = []
                    for idx, part in enumerate(in_parts):
                        if idx != i:
                            training_set_in += list(part)
                            training_set_out += list(out_parts[idx])
                
                    training_set = {"in": training_set_in, "out": training_set_out}
                    test_set = {"in": in_parts[i], "out": out_parts[i]}
                    print("[ k =", i, "]:", end=" ")
                    errors, metrics = Multilayer([5, 1], 35, params["eta"]).solve(training_set, test_set, params["error_bound"], 1)
                    all_errors.append(errors)
                    print(min(errors))
                    all_metrics.append(metrics)
                plot_all_errors(all_errors)
                plot_all_metrics(all_metrics)

            else:         
                training_set = {"in":  in_set, "out": out_set}
                test_set = {"in": [], "out": []}
                errors, metrics = Multilayer([5, 1], 35, params["eta"]).solve(training_set, test_set, params["error_bound"])   
                print(min(errors))
                plot_error(errors)


        else:
            # EJERCICIO 3: NUMERO
            # el training set es el mismo
            print("Solving number classification")
            out_set = []
            # Fills out_set
            for num in range(10):
                expected_output = [-1] * 10
                expected_output[num] = 1
                out_set.append(expected_output)
            
            # 5, 11, 10 anduvo bastante bien
            # 9, 10 funciona muy bien tambien
            multilayer = Multilayer([5, 11, 10], 35, params["eta"])
            training_set = {"in": in_set, "out": out_set}

            test_set_in = []
            test_set_out = []
            for k in range(10):
                for i, picture in enumerate(in_set):
                    picture_copy = np.copy(picture)
                    for j in range(len(picture)):
                        rnd = np.random.uniform()
                        if rnd < 0.02:
                            picture_copy[j] = 1 - picture_copy[j]
                    
                    test_set_in.append(picture_copy)
                    test_set_out.append(out_set[i])

            test_set = {"in": test_set_in, "out": test_set_out}

            errors, metrics = multilayer.solve(training_set, test_set, params["error_bound"], 0.1) 
            plot_error(errors)
            print(min(errors))
            plot_metric(metrics, len(metrics))
            print(max(metrics))

        
    
        