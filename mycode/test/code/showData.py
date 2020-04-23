import numpy as np
import matplotlib.pyplot as plt

def dataLoad(dataPath):
    data = []
    with open(dataPath, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            d = line.strip('\n').split(' ')
            data.append(np.float64(d))
    file.close()
    return np.array(data)

data1 = dataLoad(r'E:\mlcode\mycode\D1.txt')
data2 = dataLoad(r'E:\mlcode\mycode\D2.txt')
data3 = dataLoad(r'E:\mlcode\mycode\D3.txt')

fig,axes = plt.subplots(2,2)
axes[0,0].scatter(data1[:,0],data1[:,1],c='r',s=1)
axes[0,1].scatter(data2[:,0],data2[:,1],c='b',s=1)
axes[1,0].scatter(data3[:,0],data3[:,1],c='y',s=1)

plt.savefig('./data.png')

plt.show()
