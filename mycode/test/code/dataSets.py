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

def fangzhen(m,n):
    data = []
    for i in range(m):
        for j in range(n):
            list = []
            list.append(i)
            list.append(j)
            data.append(list)
    return (np.array(data))

data1 = fangzhen(20,8)
data2 = fangzhen(50,20)
data3 = fangzhen(13,30)
data8 = dataLoad(r'E:\mlcode\mycode\aaa.txt')
print(data8)




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

    data_01 = Normalized(data1)*10
    data_02 = Normalized(data2)*4
    data_02 = Move_y(data_02,6)
    data_03 = Normalized(data3)*5
    data_03 = Move_x(data_03,8)
    data_03 = Move_y(data_03,5)
    # data_04 = Normalized(data4)*1.5
    # data_04 = Move_y(data_04,4)
    # data_05 = Normalized(data5) * 1.5
    # data_05 = Move_y(data_05, 4)
    # data_05 = Move_x(data_05,2)
    # data_06 = Normalized(data6)*3
    # data_06 = Move_y(data_06, 4)
    # data_06 = Move_x(data_06, 4)
    # data_07 = Normalized(data7)*2
    # data_07 = Move_x(data_07,2)
    # data_07 = Move_y(data_07,8)


    # out_01 = np.vstack((data_01,data_02))
    # out_02 = np.vstack((out_01,data_03))
    # out_03 = np.vstack((out_02,data8))
    # out_03 = np.vstack((out_02, data_04))
    # out_04 = np.vstack((out_03, data_05))
    # out_05 = np.vstack((out_04, data_06))
    # out_06 = np.vstack((out_05, data_07))
    # np.savetxt('E:\data.txt',out_03,fmt='%f',delimiter=' ')



    pyplot.scatter(data_01[:, 0], data_01[:, 1], c='b',s=1);
    pyplot.scatter(data_02[:, 0], data_02[:, 1], c='b',s=1);
    pyplot.scatter(data_03[:, 0], data_03[:, 1], c='b',s=1);
    pyplot.scatter(data8[:, 0], data8[:, 1], c='r', s=1);
    # pyplot.scatter(data_04[:, 0], data_04[:, 1], c='r',s=3);
    # pyplot.scatter(data_05[:, 0], data_05[:, 1], c='r',s=3);
    # pyplot.scatter(data_06[:, 0], data_06[:, 1], c='r',s=3);
    # pyplot.scatter(data_07[:, 0], data_07[:, 1], c='r', s=3);
    # pyplot.scatter(out_03[:, 0], out_03[:, 1], c='r', s=1);

    pyplot.show()