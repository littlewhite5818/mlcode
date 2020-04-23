from matplotlib import pyplot
import numpy as np

def dataLoad(dataPath):
    data = []
    with open(dataPath, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            d = line.strip('\n').split('    ')
            data.append(np.float64(d))
    file.close()
    return np.array(data)

data = dataLoad(r'E:\mlcode\mycode\data.txt')
np.savetxt('E:\D3.txt',data,fmt='%f',delimiter=' ')

pyplot.scatter(data[:, 0], data[:, 1], c='b', s=1);
pyplot.show()