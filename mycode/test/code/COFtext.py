#!/usr/bin/python
# -*- coding: utf8 -*-
from numpy import *
import COF
from util import *

def data_loadDataSet():
    # fileName = 'D:\ybl_dataset_sy/ad.txt'
    fileName=r'E:\Outlier\data\vowels.txt'
    dataMat=[]
    with open(fileName) as data:
        lines=data.readlines()
        for line in lines:
            lineData=line.strip().split('\t')
            lineData=list(map(lambda x:float(x), lineData))
            dataMat.append(lineData)
    return(np.array(dataMat))

def test_COF(instances,k):
    factors=COF.outlier_factors(instances,k)
    sort_factors = argsort(factors, kind='quicksort')

    num = 97
    ot = 0
    test = [60,80,97,120]
    for i in range(len(sort_factors)):
        if sort_factors[i] < num:
            ot = ot + 1
        for j in range(len(test)):
            if i == test[j]:
                print("--top-" + str(test[j]) + "---")
                print("Re: ", ot / num)
                print("Pr: ", ot / test[j])


if __name__ == "__main__":
    instances = data_loadDataSet()
    k = 15
    print('K='+str(k))
    test_COF(instances,k)