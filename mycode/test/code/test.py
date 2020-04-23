import numpy as np
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

if __name__=='__main__':
    # data = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    # data = np.array(data)
    C1 = [1,2,3]
    # C2 = [3,4]
    # print(distC(C1,C2,data))

    min = np.argmin(C1)
    print(min)

