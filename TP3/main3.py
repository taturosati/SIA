from multilayer import Multilayer
from plotter import plot_error


or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
or_out_set = [[1], [1], [-1], [-1]]
print("XOR")

# errors = Multilayer([2, 1], 2, 0.5).solve(or_in_set, or_out_set, 0.001)
# plot_error(errors)

# EJERCICIO 2: PAR O IMPAR

training_set = []
with open("./number_set.txt", "r") as training_file:
        readlines = training_file.readlines()
        for idx in range(int(len(readlines) / 7)):
            line_range = readlines[idx * 7 : (idx + 1) * 7]
            num_array = [-1]
            for line in line_range:
                num_array +=  [int(n) for n in line.split()]
            training_set.append(num_array)
            # training_set.append(line_range)
            
        training_file.close()

# print(training_set)

# out_set = list(range(10))
out_set = [1,-1] * 5
# print(out_set)


# errors = Multilayer([11, 10, 2], 2, 0.5).solve(training_set, out_set, 0.001)

# EJERCICIO 3: NUMERO
# el training set es el mismo

out_set = []
for num in range(10):
    expected_output = [0] * 10
    expected_output[num] = 1
    out_set.append(expected_output)

errors = Multilayer([11, 10], 35, 0.1).solve(training_set, out_set, 0.01)
plot_error(errors)
