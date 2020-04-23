import numpy as np
import matplotlib.pyplot as plt

# 随机生成1000个点，围绕在y=0.1x+0.3的直线周围
from sklearn.datasets import make_circles, make_moons


def dataLoad(dataPath):
    data = []
    with open(dataPath, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            d = line.strip('\n').split('    ')
            data.append(np.float64(d))
    file.close()
    return np.array(data)

num_points = 300
vectors_set_1 = []
vectors_set_2 = []
for i in range(num_points):
    x1 = np.random.uniform(10.00, 20.00)
    y1 = x1+ np.random.normal(0.0, 0.05)
    vectors_set_1.append([x1, y1])
    x2 = x1
    y2 = -x2 + 20+ np.random.normal(0.0, 0.05)
    vectors_set_2.append([x2, y2])
data1 = np.array(vectors_set_1)
data2 = np.array(vectors_set_2)
data3,target3= make_circles(n_samples=500,shuffle=True,noise=0.1,random_state=0)
print(target3)
# data3,target3= make_circles(n_samples=300,shuffle=False,noise=0.1,random_state=0)
data4 = dataLoad(r'E:\mlcode\mycode\data.txt')

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
data_01 = data1
data_02 = data2
data_03 = Normalized(data3)*2
data_03 = Move_y(data_03,10)
data_04 = data4

out_01 = np.vstack((data_01,data_02))
out_02 = np.vstack((out_01,data_03))
out_03 = np.vstack((out_02,data_03))
out_04 = np.vstack((out_03,data_04))



plt.scatter(data1[:, 0], data1[:, 1], c='b',s=1);
plt.scatter(data2[:, 0], data2[:, 1], c='b',s=1);
plt.scatter(data_03[:, 0], data_03[:, 1], c='b',s=1);
plt.scatter(data4[:, 0], data4[:, 1], c='r',s=1);

# plt.scatter(out_04[:, 0], out_04[:, 1], c='r',s=1);
# np.savetxt('E:\D2.txt',out_04,fmt='%f',delimiter=' ')

plt.show()