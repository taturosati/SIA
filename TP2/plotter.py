from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


# x1 = [1,2,3,4,5]
# y1 = [3,5,4,7,3]
# x2 = [1,2,3,4,5]
# y2 = [2,4,3,5,3]
  
# # plot lines
# plt.plot(x1, y1, label = "max")
# plt.plot(x2, y2, label = "avg")
# plt.legend()
# plt.show()

def plot(arr):
    # max_x = []
    max_y = []
    # avg_x = []
    avg_y = []
    for a in arr:
        if a[2] == 'max':
            # max_x.append(a[0])
            max_y.append(a[1])
        else:
            # avg_x.append(a[0])
            avg_y.append(a[1])

    x = range(len(max_y))


    
    plt.figure(figsize=(5, 2.7), layout='constrained')         
    ax = plt.gca()
    ax.locator_params('y', nbins=5000)   
    ax.plot(x, max_y, label = "max")
    ax.plot(x, avg_y, label = "avg")

    

    # plt.yticks(np.arange(min(avg_y), max(max_y)+1, 1.0))
    plt.show()

# my_arr = [[1,2, "max"], [2, 4, "max"], [1,1, "avg"], [2, 3, "avg"]]
# plot(my_arr)

