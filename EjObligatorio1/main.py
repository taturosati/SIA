from solver import Solver
import time

def print_result(result, time):
    arr = result[0]
    W = [arr[i] for i in range(0,3)]
    w = [[], []]
    w[0] = [arr[i] for i in range(3,6)]
    w[1] = [arr[i] for i in range(6,9)]
    w0 = [arr[i] for i in range(9,11)]

    print("Time:", time)
    print("Optimal solution")
    print("- W:", W)
    print("- w:", w)
    print("- w0:", w0)
    print("- Error:", result[1])


inset = [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.883]]
correct_output = [0,1,1]

print("Gradient Descent: ")
start_time = time.time()
result = Solver(inset, correct_output).gradient_minimizer()
print_result(result, time.time() - start_time)

print("Conjugate Gradient: ")
start_time = time.time()
result = Solver(inset, correct_output).conjugate_gradient_minimizer()
print_result(result, time.time() - start_time)

print("ADAM:")
start_time = time.time()
result = Solver(inset, correct_output).adam_minimizer()
print_result(result, time.time() - start_time)

