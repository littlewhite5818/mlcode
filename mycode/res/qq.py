# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
def fangzhen(m,n):
    data = []
    for i in range(m):
        for j in range(n):
            list = []
            list.append(i)
            list.append(j)
            data.append(list)
    return (np.array(data))

if __name__ == '__main__':
    data_01 = fangzhen(10,2)
    print(data_01)
    plt.scatter(data_01[:, 0], data_01[:, 1], c='y');
    plt.show()


