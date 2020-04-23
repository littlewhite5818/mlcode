# encoding: utf-8
from sklearn.neighbors import NearestNeighbors
from collections import Counter
import numpy as np
from matplotlib import pyplot as plt

'''
计算knn
'''
def computeKnn(k, data):
    nbrs = NearestNeighbors(n_neighbors=k+1, algorithm='auto').fit(data)
    distances, indices = nbrs.kneighbors(data)
    knnMatrix = [indices, distances]
    return knnMatrix

'''
计算某点P的局部可达密度
'''
def reachDensity(pIndex, knnMatrix, minPts):
    flag = 1
    sumReachDist = 0
    while flag < minPts:
        index_o = knnMatrix[0][pIndex][flag]
        dist_po = knnMatrix[1][pIndex][flag]
        minPts_dist_o = knnMatrix[1][index_o][-1]
        reach_Dist_p = max(dist_po, minPts_dist_o)
        sumReachDist = sumReachDist + reach_Dist_p
        flag = flag+1
    lrd = (minPts-1)/sumReachDist
    return lrd

'''
计算某点的离群因子LOF
'''
def computeLOF(pIndex,knnMatrix, minPts, lrdMat):
    lrd_p = lrdMat[pIndex]
    flag = 1
    lrd_op_sum = 0
    while flag < minPts:
        index_o = knnMatrix[0][pIndex][flag]
        lrd_o = lrdMat[index_o]
        lrd_op_sum = lrd_op_sum + lrd_o/lrd_p
        flag = flag+1
    lof_p = lrd_op_sum/(minPts-1)
    return lof_p


def getlrdMat(n, knnMatrix, k):
    lrd = []
    for i in range(n):
        lrd_i = reachDensity(i, knnMatrix, k)
        lrd.append(lrd_i)
    return lrd

def getLofMat(n, knnMatrix, lrdMat, k):
    lofMat = []
    for i in range(n):
        lof_i = computeLOF(i,knnMatrix, k, lrdMat)
        lofMat.append(lof_i)
    return lofMat


def isDirectReachability(cp, p, lrdMat, pct):
    if lrdMat[cp] > lrdMat[p]/(1+pct) and lrdMat[cp] < lrdMat[p]*(1+pct):
        return True
    else:
        return False


def expandCluster(n,i,cid,pct, k, label, knnMatrix, lrdMat):
    label[i] = cid
    tempVector = []
    for kn in range(1, k+1):
        cp = knnMatrix[0][i][kn]
        if label[cp] in [-1,0] and isDirectReachability(cp, i, lrdMat, pct):
            tempVector.append(cp)
            label[cp] = cid
    while len(tempVector) > 0:
        i = tempVector.pop(0)
        for kn in range(1, k+1):
            cp = knnMatrix[0][i][kn]
            if label[cp] in [-1, 0] and isDirectReachability(cp, i, lrdMat, pct):
                tempVector.append(cp)
                label[cp] = cid



def ldbscan(n,dataset, knnMatrix, lofub,pct,k):
    label = [-1 for i in range(n)]
    lrdMat = getlrdMat(n, knnMatrix, k)
    lofMat = getLofMat(n,knnMatrix,lrdMat,k)
    cid = 0
    for i in range(n):
        if label[i] == -1:
            if lofMat[i] <= lofub:
                cid = cid + 1
                expandCluster(n,i,cid,pct, k, label, knnMatrix, lrdMat)
            else:
                label[i] = 0
    return label,lrdMat,lofMat

def dataLoad(dataPath):
    data = []
    with open(dataPath, mode='r', encoding='utf-8') as file:
        for line in file.readlines():
            d = line.strip('\n').split('\t')
            data.append(np.float64(d))
    file.close()
    return np.array(data)

def ubcbo(n,c_count,alpha):
    for i in range(len(c_count)):
        sum = 0
        for j in range(i + 1):
            sum = sum + c_count[j]
        if (sum >= n * alpha and sum - c_count[j] <= n * alpha):
            return i
def devide(c_label,data_label):
    C =[]
    for j in range(len(c_label)):
        temp = []
        for k in range(len(data_label)):
            if c_label[j] == data_label[k]:
                temp.append(k)
        C.append(temp)
    return C
def getDistBetweenPoints(point1, point2):
    dist = np.sqrt(np.sum(np.square(np.subtract(point1, point2))))
    return dist

def distC(C1,C2,data):
    x = len(C1)
    y = len(C2)
    dict_mat = np.zeros((x,y))
    for i in range(len(C1)):
        for j in range(len(C2)):
            dist_temp = getDistBetweenPoints(data[C1[i]],data[C2[j]])
            dict_mat[i][j] = dist_temp
    min_dist = dict_mat.min()
    return min_dist

def Lrd(C2,lrd):
    len_C2 = len(C2)
    sum = 0
    for i in C2:
        sum = sum +lrd[i]
    return sum/len_C2


if __name__ == '__main__':
    dataset = dataLoad(r'E:\mlcode\mycode\test\data\optdigits_150.txt')
    n = len(dataset)
    # alpha_list = [0.75,0.8,0.85,0.9,0.95]
    # for alpha in alpha_list:
    alpha = 0.9
    lofub = 1
    pct = 0.2
    k = 20
    minpts = 3

    knnMatrix = computeKnn(k,dataset)
    label ,lrdmat,lofmat =  ldbscan(n,dataset,knnMatrix,lofub,pct,minpts)
    label_count = Counter(label)



    key = list(label_count.keys())
    value = list(label_count.values())

    matrix = []
    for i in range(len(key)):
        temp = []
        temp.append(key[i])
        temp.append(value[i])
        matrix.append(temp)
    matrix = np.array(matrix)
    matrix_sort = matrix[np.lexsort(-matrix.T)]

    c = matrix_sort[:,0]
    c_count = matrix_sort[:,1]
    C = devide(c,label)                 #划分C

    ubc = ubcbo(n,c_count,alpha)+1     #计算离群簇在C中起始坐标
    cluster_label = c[ubc:]            #统计离群标签

    C_nomal = []
    C_abnomal = []
    for i in range(len(C)):
        if i<ubc:
            C_nomal.append(C[i])
        else:
            C_abnomal.append(C[i])      #分出正常簇，离群簇

    min_C = []
    for i in range(len(C_abnomal)): #距离离群簇最近的正常簇
        for j in range(len(C_nomal)):
            dist = []
            dist.append(distC(C_abnomal[i],C_nomal[j],dataset))
            min = np.argmin(dist)
        min_C.append(min)

    factors = []
    for i in range(len(C_abnomal)):
        C1 = C_abnomal[i]
        C2 = C_nomal[min_C[i]]
        dist_C1_C2 = distC(C1,C2,dataset)
        factor = len(C1)*dist_C1_C2*Lrd(C2,lrdmat)
        factors.append(factor)



    for i in range(len(factors)):
        for j in range(len(C_abnomal[i])):
            lofmat[C_abnomal[i][j]]=factors[i]

    matrix_factor = np.array([[i,lofmat[i] ] for i in range(len(lofmat))])
    factor_sort = matrix_factor[np.lexsort(-matrix_factor.T)]
    factor_sort_list = factor_sort[:,0]

    m = [50, 100, 180, 250, 300, 320]
    n = 0
    num = 150
    rankPower = 0
    Recall = 0
    Prcesion = 0
    sum = 0
    for i in range(1, len(factor_sort_list) + 1):
        if 0 <= factor_sort_list[i - 1] < num:
            sum = sum + i
            n = n + 1
        if i in m:
            Recall = n / num
            Prcesion = n / i
            if sum == 0:
                print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2),
                      " RankPower: - ")
            else:
                rankPower = (n * (n + 1)) / (2 * sum)
                print("top-", i, "n: ", n, " Recall : ", round(Recall, 2), "  Precsion: ", round(Prcesion, 2),
                      " RankPower: ", round(rankPower, 2))

    # np.savetxt(r'C:\Users\zz\Desktop\res\cbof\vowels1.txt', factor_sort_list, fmt='%f', delimiter=' ')
    # out = []
    # for i in range(len(factor_sort_list)):
    #     for j in range(len(C_abnomal[i])):
    #         out.append(C_abnomal[i][j])

    # plt.scatter(dataset[:,0] , dataset[:,1] , c = 'b',s=1)
    # for i in out:
    #     plt.scatter(dataset[i,0] , dataset[i,1] , c = 'r',s=20,marker='*')
    # plt.title('k=20,pct=0.3,MinP=20,LOFUB=1,alpha=0.90', fontsize='large')
    # plt.show()
    # correct = 0
    # for i in  range(len(out)):
    #     if out[i] < outlier_num:
    #         correct +=1                  #统计真离群点个数

    # print('分类情况:')
    # print(label_count)
    # print('alpha='+str(alpha)+'  lofub = '+str(lofub)+'  pct=' + str(pct)+'  k='+str(k)+'  minpts='+str(minpts))
    # print('检测出的离群点个数：'+str(len(out)))
    # print('检测出的真离群点个数：' + str(correct))
#     print('Re:'+str(correct/outlier_num))
#     if len(out)==0:
#         print('PR:0')
#     else:
#         print('PR:' + str(correct / len(out)))