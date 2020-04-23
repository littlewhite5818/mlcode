#!/usr/bin/python
# -*- coding: utf8 -*-
from numpy import *
import DB
from util import *
import datetime
from itertools import islice

def data_loadDataSet():
    fileName = r'E:\Outlier\data\musk.txt'
    dataMat=[]
    with open(fileName) as data:
        lines=data.readlines()
        for line in lines:
            lineData=line.strip().split('\t')
            lineData=list(map(lambda x:float(x), lineData))
            dataMat.append(lineData)
    return(np.array(dataMat))


def test_DB(instances,k):
    factors=DB.outlier_factors(instances,k)
    sort_factor = argsort(factors, kind='quicksort')
    sort_factors = sort_factor[::-1]

    num = 97
    ot = 0
    test = [60, 80, 97, 120]
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
    k_list = [10,15,20,25,30]
    for k in k_list:
        print('K=' + str(k))
        test_DB(instances,k)
