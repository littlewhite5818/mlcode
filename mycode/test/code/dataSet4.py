import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_blobs, make_moons


def dataLoad(dataPath):
    data = []
    with open(dataPath, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            d = line.strip('\n').split('   ')
            data.append(np.float64(d))
    file.close()
    return np.array(data)

def fangzhen(m,n):
    data = []
    for i in range(m):
        for j in range(n):
            list = []
            list.append(i)
            list.append(j)
            data.append(list)
    return (np.array(data))


def Normalized(data):
    data_01 = np.array(data)
    data_max = data_01.max()
    data_min = data_01.min()
    data_02 = data/(data_max-data_min)
    return data_02

def Move_x(data,n):
    distMatrix = [[n, 0] for i in range(len(data))]
    return data+distMatrix

def Move_y(data,n):
    distMatrix = [[0, n] for i in range(len(data))]
    return data+distMatrix

if __name__ == '__main__':
    data1 = fangzhen(5, 5)
    data2, target2 = make_blobs(n_samples=200, n_features=2, random_state=0, centers=1,
                                cluster_std=0.2)
    data3, target3 = make_blobs(n_samples=200, n_features=2, random_state=0, centers=1,
                                cluster_std=0.6)
    data4, target4 = make_moons(n_samples=200, shuffle=True, noise=0.1, random_state=0)
    data5 = dataLoad(r'E:\mlcode\mycode\data.txt')

    data_01 = Normalized(data1)
    data_01 = Move_y(data_01, 3)
    data_01 = Move_x(data_01, 3)
    data_02 = data2
    data_03 = data3
    data_03 = Move_y(data_03,-5)
    data_03 = Move_x(data_03,3)
    data_04 = data4
    data_04 = Move_y(data_04,1)
    data_05 = data5

    out_01 = np.vstack((data_01, data_02))
    out_02 = np.vstack((out_01, data_03))
    out_03 = np.vstack((out_02, data_03))
    out_04 = np.vstack((out_03, data_04))
    out_05 = np.vstack((out_04, data_05))

    # plt.scatter(data_01[:, 0], data_01[:, 1], c='b', s=10)
    # plt.scatter(data_02[:, 0], data_02[:, 1], c='b', s=10)
    # plt.scatter(data_03[:, 0], data_03[:, 1], c='b', s=10)
    # plt.scatter(data_04[:, 0], data_04[:, 1], c='b', s=10)
    # plt.scatter(data_05[:, 0], data_05[:, 1], c='r', s=10)
    plt.scatter(out_05[:, 0], out_05[:, 1], c='r', s=10)
    np.savetxt('E:\data.txt', out_05, fmt='%f', delimiter=' ')

    plt.show()