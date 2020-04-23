# -*- coding: utf-8 -*-
from __future__ import division
import util

def outlier_factors(instances, k):
    """Compute the factors for each instance in instances.
    Factor is the average of distances between instance and it's kNN
    Return: factors
    """
    factors = []
    for instance in instances:
        (k_distance, kNN) = util.k_nearest_neighbors(instances, instance, k)
        factor = 0
        for neighbor in kNN:
            factor += util.distance_euclidean(instance, neighbor)
        factor = factor/k
        factors.append(factor)
    return factors

def outlier_factors_withkNNdic(instances, kNNdict, k):
    """Compute the factors for each instance in instances.
    Factor is the average of distances between instance and it's kNN
    Return: factors
    """
    factors = []
    for i in range(len(instances)):
        instance = instances[i]
        kNN = kNNdict[i]
        factor = 0
        for j in kNN:
            neighbour = instances[j]
            factor += util.distance_euclidean(instance, neighbour)
        factor = k / factor
        factors.append(factor)
    return factors
