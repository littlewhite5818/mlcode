# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 01:03:13 2018

@author: sbml1
"""
import numpy as np
from scipy.stats import norm
from math import isnan

def distance_euclidean(instance1, instance2):
    """Computes the distance between two instances. Instances should be arrays of equal length.
    Returns: Euclidean distance
    """
    # check if instances are of same length
    if len(instance1) != len(instance2):
        raise AttributeError("Instances have different number of arguments.")

    distance = np.linalg.norm(instance1 - instance2)
    return distance


def k_nearest_neighbors(instances, instance, k):
    """Computes the k-distance of instance as defined in paper. It also gatheres the set of k-distance neighbours.
    Returns: (k-distance, k-distance neighbours)"""
    distances = {}
    for instance2 in instances:
        distance_value = distance_euclidean(instance, instance2)
        if distance_value in distances:
            distances[distance_value].append(instance2)
        else:
            distances[distance_value] = [instance2]
    distances = sorted(distances.items())
    neighbours = []
    k_distance_value = 0
    for i in range(1, len(distances)):
        neighbours.extend(distances[i][1])
        # extend()在列表末尾一次性追加另一个序列中的多个值
        if len(neighbours) == k:
            k_distance_value = distances[i][0]
            break
        elif len(neighbours) > k:
            k_distance_value = distances[i - 1][0]
            break
    return k_distance_value, neighbours


def kNN_dic(instances, k):
    """Computes the kNN for each instance
    Retrun: dic{instanceNo,kNNNos}
    instanceNo means the sort instance in instances
    kNNNos means the numbers of kNN
    """
    dic = {}
    N = len(instances)
    for i in range(N):
        p = instances[i]
        distances = {}
        for j in range(N):
            q = instances[j]
            distance_value = distance_euclidean(p, q)
            if distance_value in distances:
                distances[distance_value].append(j)
            else:
                distances[distance_value] = [j]
        distances = sorted(distances.items())
        neighbours = []
        for m in range(1, len(distances)):
            neighbours.extend(distances[m][1])
            if len(neighbours) >= k:
                break
        dic[i] = neighbours
        # print dic
    return dic


def suspected_of_fraud(factors, a, b):
    """Judge if any factor>threshold
    threshold=a*mean+b*std
    """
    narray = np.array(factors)
    sum1 = narray.sum()
    narray2 = narray * narray
    sum2 = narray2.sum()
    mean = sum1 / len(factors)
    std = sum2 / len(factors) - mean ** 2
    threshold = a * mean + b * std
    for factor in factors:
        if factor > threshold:
            return True
    return False


def score_of_fraud(factors):
    """Judge if any factor>threshold
    threshold=mean+2.58std =>99
    threshold=mean+1.96std =>95
    threshold=mean+std =>68
    """
    result = 0
    narray = np.array(factors)
    sum1 = narray.sum()
    narray2 = narray * narray
    sum2 = narray2.sum()
    mean = sum1 / len(factors)
    std = sum2 / len(factors) - mean ** 2
    if std == 0:
        x = 0  # 方差为零，每个点的离群度相同
    else:
        x = (max(factors) - mean) / std
    result = norm.cdf(x) - norm.cdf(-x)
    if isnan(result):
        return 0
    return int(100 * result)

