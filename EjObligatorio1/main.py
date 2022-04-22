from solver import Solver

inset = [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.883 ]]
correct_output = [0,1,1]

# reactive = [W0,W1, W2, w11,w12,w13,w21,w22,w23, w01,w02]
# W = [reactive[0],reactive[1], reactive[2]]
# w = [[reactive[3],reactive[4],reactive[5]],[reactive[6],reactive[7],reactive[8]]]
# w0 = [reactive[9],reactive[10]]

result = Solver(inset, correct_output).conjugate_gradient_minimizer()
print(result)