from multilayer import Multilayer


or_in_set = [[-1, -1, 1], [-1, 1, -1], [-1, -1, -1], [-1, 1, 1]]
or_out_set = [[1], [1], [-1], [-1]]
print("XOR")

Multilayer([2, 1], 2).solve(or_in_set, or_out_set, 0.001)
