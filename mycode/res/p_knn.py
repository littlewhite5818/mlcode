import numpy as np
from sklearn.neighbors import NearestNeighbors
import time
import matplotlib.pyplot as plt

def knn_mean(data,k):
    row = data.shape[0]
    neigh = NearestNeighbors(n_neighbors=k)   # k近邻的k个数
    neigh.fit(data)                           # 数据矩阵
    mean = []
    for i in range(row):
        array = neigh.kneighbors([data[i,:]])[1][0]    # k近邻的索引数组
        out_01 = np.array([data[int(o)] for o in array])
        mean_01 = (out_01.sum(axis=0))/k                       #根据索引 按行相加 取平局值
        mean.append(mean_01)
    return np.array(mean)                #返回质心矩阵


def join(data,array):
    matrix = np.row_stack((data,array))
    return matrix


def order(data,mean):
    r_o_dist = []
    for i in range(len(data)):
        new_matrix = join(data,mean[i])     #质心连入矩阵
        dist_matrix_p = getDistDataSetToPoint(new_matrix,new_matrix[i])
        order_a = dist_matrix_p[np.lexsort(dist_matrix_p.T)][:,0]
        dist_matrix_cord = getDistDataSetToPoint(new_matrix,new_matrix[-1])
        order_b = dist_matrix_cord[np.lexsort(dist_matrix_cord.T)][:,0]
        o_b_a,d_a_b = d_ab(order_a,order_b)     #计算Oa(b)和a在b中的累加和
        o_a_b,d_b_a = d_ab(order_b,order_a)     #计算Ob(a)和b在a中的累加和
        D_ab = (d_b_a+d_a_b)/(min(o_a_b,o_b_a))
        r_o_dist.append(D_ab)
    return r_o_dist


def d_ab(order_a,order_b):
    for i in range(len(order_a)):
        if order_a[i] == order_b[0]:
            pos = i                    #记录b在a中位置
            break
    d_a_b = 0
    for i in range(pos):
        for j in range(len(order_b)):
            if order_b[j] == order_a[i]:
                d_a_b = d_a_b +j
                break
    return pos,d_a_b


def dataLoad(dataPath):
    data = []
    with open(dataPath, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            d = line.strip('\n').split(' ')
            data.append(np.float64(d))
    file.close()
    return np.array(data)


def getDistBetweenPoints(point1, point2):
    dist = np.sqrt(np.sum(np.square(np.subtract(point1, point2))))
    return dist


def getDistDataSetToPoint(dataSet, point):
    distMatrix = [[i+1, 0] for i in range(len(dataSet))]
    for i in range(len(dataSet)):
        dist_i = getDistBetweenPoints(point, dataSet[i])
        distMatrix[i][1] = dist_i
    return np.array(distMatrix)


def rank_order_dist(k,n):
    starttime = time.time()
    data = dataLoad(r'E:\data.txt')
    mean = knn_mean(data,k)
    r_o_dist = order(data,mean)
    distMatrix = [[i, 0] for i in range(len(r_o_dist))]          # 结果排序
    for i in range(len(r_o_dist)):
        distMatrix[i][1] = r_o_dist[i]
    order_list_begin = np.array(distMatrix)
    order_list_mid = order_list_begin[np.lexsort(order_list_begin.T)][:, 0]
    order_list_end = order_list_mid[-n:]
    endtime1 = time.time()
    dtime1 = endtime1 - starttime
    print(order_list_end)
    out = np.array([data[int(o)] for o in order_list_end])
    plt.scatter(data[:, 0], data[:, 1], s=7, color='b')
    plt.scatter(out[:, 0], out[:, 1], s=7, color='r')
    plt.show()
    print("程序运行时间：%.8s s" % dtime1)


if __name__=='__main__':
     rank_order_dist(20,42)

