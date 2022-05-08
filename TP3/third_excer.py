from plotter import plot_all_errors, plot_all_metrics
from utils import Utils
from multilayer import Multilayer
from plotter import plot_error, plot_metric
import numpy as np

def check_prediction(multilayer, in_set, out_set):
    pe = 0
    nope = 0
    for i, in_ix in enumerate(in_set):
        res = multilayer.predict(in_ix)
        for n in np.subtract(out_set[i], np.array(res)):
            if abs(n) > 0.2:
                nope+=1
                break
        pe+=1

def third_excercise(params: dict):
    if params["item"] == "a":
        or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
        or_out_set = [[1], [1], [-1], [-1]]
        training_set = {"in": or_in_set, "out":or_out_set}
        test_set = {"in": [], "out":[]}
        print("Solving for XOR")

        errors, metrics = Multilayer([2, 1], 2, params["eta"]).solve(training_set, test_set, params["error_bound"])
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

            met = []
            best_metric = [0]
            all_errors = []
            all_metrics = []

            # TODO: ver cuando hacer y no hacer la validacion cruzada
            if params["validation"] == True:
                for i in range(k):
                    training_set_in = []
                    training_set_out = []
                    for idx, part in enumerate(in_parts):
                        if idx != i:
                            training_set_in += list(part)
                            training_set_out += list(out_parts[idx])
                
                    training_set = {"in":  training_set_in, "out": training_set_out}
                    test_set = {"in": in_parts[i], "out": out_parts[i]}
                    # print(test_set)
                    # print("[ k =", i, "]:", end=" ")
                    errors, metrics = Multilayer([5, 1], 35, params["eta"]).solve(training_set, test_set, params["error_bound"])
                    all_errors.append(errors)
                    all_metrics.append(metrics)
                plot_all_errors(all_errors)
                plot_all_metrics(all_metrics)


            # if max(metrics) > max(best_metric):
            #     print("METRICA:", max(metrics))
            #     best_metric = metrics
            else:         
                training_set = {"in":  in_set, "out": out_set}
                test_set = {"in": [], "out": []}
                errors, metrics = Multilayer([5, 1], 35, params["eta"]).solve(training_set, test_set, params["error_bound"])   
                plot_error(errors)

        else:
            # EJERCICIO 3: NUMERO
            # el training set es el mismo
            print("Solving number classification")
            out_set = []
            # Fills out_set
            for num in range(10):
                expected_output = [0] * 10
                expected_output[num] = 1
                out_set.append(expected_output)
            
            # 5, 11, 10 anduvo bastante bien
            # 9, 10 funciona muy bien tambien
            multilayer = Multilayer([5, 11, 10], 35, params["eta"])
            training_set = {"in": in_set, "out": out_set}
            test_set = {"in": [], "out": []}
            errors, metrics = multilayer.solve(training_set, test_set, params["error_bound"]) 
            plot_error(errors)
            plot_metric(metrics)

            print("Antes de agregar ruido")
            check_prediction(multilayer, in_set, out_set)

            # agregamos ruido a los datos
            for i, picture in enumerate(in_set):
                for j in range(len(picture)):
                    rnd = np.random.uniform()
                    if rnd < 0.02:
                        picture[j] = 1 - picture[j]

            print("Despues de agregar ruido")
            check_prediction(multilayer, in_set, out_set)


        
    
        