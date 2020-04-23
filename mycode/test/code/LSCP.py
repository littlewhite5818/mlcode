#!/usr/bin/python
# -*- coding: utf8 -*-
from pyod.models.lscp import LSCP
from pyod.models.lof import LOF
from pyod.utils.utility import standardizer
from numpy import *
import numpy as np
import time
from pyod.utils.data import generate_data
starttime = time.time()

def data_loadDataSet():
    fileName=r'E:\mlcode\mycode\test\data\D1_45.txt'
    dataMat=[]
    with open(fileName) as data:
        lines=data.readlines()
        for line in lines:
            lineData=line.strip().split(' ')
            lineData=list(map(lambda x:float(x), lineData))
            dataMat.append(lineData)
    return(np.array(dataMat))

data=data_loadDataSet()

X_train, y_train, X_test, y_test = generate_data(
    n_train=50, n_test=50,
    contamination=0.1, random_state=42)
X_train, X_test = standardizer(X_train, X_test)
detector_list = [LOF(n_neighbors=10), LOF(n_neighbors=15)]
clf = LSCP(detector_list)
clf.fit(X_train)
clf.fit(data)
y_train_scores = clf.decision_scores_

sort_factor = argsort(y_train_scores, kind='quicksort')
print(sort_factor)
sort_factors = sort_factor[::-1]
print(sort_factors)
np.savetxt(r'C:\Users\zz\Desktop\res\lscp\D1_2.txt', sort_factors, fmt='%f', delimiter=' ')

# count = 0
# num = 97
# ot = 0
# correct_pos = []
# test = [60,80,97,120]
# for i in range(len(sort_factors)):
#     if sort_factors[i] < num:
#         ot = ot + 1
#         correct_pos.append(i)
#     for j in range(len(test)):
#         if i == test[j]:
#             print("--top-" + str(test[j]) + "---")
#             print("Re: ", ot / num)
#             print("Pr: ", ot / test[j])
#             print("Rp: ",(ot*(ot+1))/(2*sum(correct_pos)))
#
# endtime1 = time.time()
# dtime1 = endtime1 - starttime
# print("程序运行时间：%.8s s" % dtime1)

