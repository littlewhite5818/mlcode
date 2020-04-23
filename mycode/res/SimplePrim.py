# encoding:utf-8
import math
import sys

'''
计算两点间距离
'''
def getDistBetweenPoints(point1, point2):
    dist = 0
    for d in range(len(point1)):
        dd = point1[d]-point2[d]
        dist = dist + dd*dd
    dist = math.sqrt(dist)
    return dist


class SimeplePrim:
    def __init__(self, dataSet):
        self.vertex = dataSet
        self.curr = 0
        self.vertex_notInTree = [i for i in range(1, len(self.vertex))]
        self.dist = [sys.maxsize]*len(self.vertex)
        self.edge_parent = [-1]*len(self.vertex)      # 存放父亲节点

    def createMST(self):
        """
        1.Update 2.Scan 3.Add
        """
        # 当图中所有的点都并到 vertexInTree时，终止循环
        while self.vertex_notInTree:
            # 1.Update 更新dist和parent列表
            lastVtIntree = self.vertex[self.curr]
            for j in self.vertex_notInTree:
                ptNotIntree = self.vertex[j]
                edge_ptTovt = getDistBetweenPoints(lastVtIntree, ptNotIntree)
                if edge_ptTovt < self.dist[j]:
                    self.dist[j] = edge_ptTovt
                    self.edge_parent[j] = self.curr
            # 2. Scan扫描dist，找到权值最短的且顶点不在tree中的点加入到tree中
            minEdge = sys.maxsize
            for j in self.vertex_notInTree:
                EdgeToTree = self.dist[j]
                if EdgeToTree <= minEdge:
                    minEdge = EdgeToTree
                    self.curr = j
            # 3.Add 将dist最小的索引对应的点加入到Intree中，并从NotIntree中移除
            # print('第' + str(addVtIndex) + '个点加入，' + '权值为：' + str(minEdge) + '--' + str(self.dist[addVtIndex]))
            self.vertex_notInTree.remove(self.curr)

