from utils import Utils
from multilayer import Multilayer
from plotter import plot_error, plot_metric
import numpy as np

ej = 3

if ej == 1:
    or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
    or_out_set = [[1], [1], [-1], [-1]]
    print("XOR")

    errors = Multilayer([2, 1], 2, 0.5).solve(or_in_set, or_out_set, 0.001)
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
    if ej == 2:
        # EJERCICIO 2: PAR O IMPAR

        out_set = [[1],[-1]] * 5

        in_set, out_set = Utils.shuffle_two_arrays(in_set, out_set)

        training_set = {"in": in_set[:8], "out": out_set[:8]}
        test_set = {"in": in_set[8:], "out": out_set[8:]}


        multi =  Multilayer([5,1], 35, 0.5)
        n = 0
        met = []
        while n < 10:
            multi.solve(training_set["in"], training_set["out"], 0.001)
            # errors = multi.solve(test_set["in"], test_set["out"], 0.001)

            pe = 0
            nope = 0

            for i in range(len(test_set["out"])):
                res = multi.predict(test_set["in"][i])
                if (test_set["out"][i] >= 0 and res[0] >= 0) or (test_set["out"][i] < 0 and res[0] < 0):
                    pe+=1
                    print("pega")
                else:
                    print("no pega")
                    nope+=1
            n+=1
            met.append(pe/(pe+nope))

        # plot_error(errors)
        plot_metric(met, 10)

    else:
        # EJERCICIO 3: NUMERO
        # el training set es el mismo
        
        ## PRINTS INTERFERENCE NUMBER ##
        # for i, picture in enumerate(in_set):
        #     picture = picture[1:]
        #     for j in range(len(picture)):
        #         rnd = np.random.uniform()
        #         if rnd < 0.02:
        #             picture[j] = 1 - picture[j]
        #         if j % 5 == 0:
        #             print()
        #         else:
        #             print(picture[j], end=" ")
        #     print()


        out_set = []
        for num in range(10):
            expected_output = [0] * 10
            expected_output[num] = 1
            out_set.append(expected_output)
        # 5, 11, 10 anduvo bastante bien
        multilayer = Multilayer([5,11,10], 35, 0.1)
        errors = multilayer.solve(in_set, out_set, 0.01) 
        plot_error(errors)

        print(in_set)

        # agregamos ruido a los datos
        for i, picture in enumerate(in_set):
            for j in range(len(picture)):
                rnd = np.random.uniform()
                if rnd < 0.02:
                    picture[j] = 1 - picture[j]
                print[j]
            print()
        # print(in_set)


        pe = 0
        nope = 0
        for i, in_ix in enumerate(in_set):
            res = multilayer.predict(in_ix)
            
            
            if (sum([abs(n) for n in np.subtract(out_set[i], np.array(res))]) <= 0.01):
                pe+=1
                print("pega")
            else:
                print("no pega")
                nope+=1

        
    
        