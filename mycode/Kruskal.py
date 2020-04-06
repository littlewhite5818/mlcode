# encoding:utf-8

class Kruskal:

    def __init__(self, data):
        self.nodenum = len(data)

    def createMST(self, edgeList):
        res = []
        # 判断点的个数 和 边数是否符合连通图的要求
        if self.nodenum <= 0 or len(edgeList) < self.nodenum - 1:
            return res

        edgeList.sort(key=lambda x: x[2])
        # print(edgeList)
        group = [[i] for i in range(self.nodenum)]
        # print(len(group))
        for edge in edgeList:
            m = -1
            n = -1
            for i in range(len(group)):
                if edge[0] in group[i]:
                    m = i
                if edge[1] in group[i]:
                    n = i
                if m != -1 and n != -1:
                    break
            if m != n:
                res.append(edge)
                group[m] = group[m] + group[n]
                group[n] = []
        return res





