import util

def ac_dist(instance,kNN,k):
    acdist=0
    for i in range(len(kNN)):
        acdist+=util.distance_euclidean(instance,kNN[i])*(k+1-i)
    acdist=(k*k+k)/acdist*2
    return acdist

def outlier_factors(instances,k):
    """Compute the factors for each instance in instances.
    Return: factors
    """
    factors=[]
    for instance in instances:
        (k_distance,kNN)=util.k_nearest_neighbors(instances,instance,k)
        cof=ac_dist(instance,kNN,k)
        factors.append(cof)
    return factors

def outlier_factors_withkNNdic(instances,kNNdict,k):
    """Compute the factors for each instance in instances.
    Return: factors
    """
    factors=[]
    for i in range(len(instances)):
        instance=instances[i]
        kNNNos=kNNdict[i]
        kNN=[]
        for j in kNNNos:
            kNN.append(instances[j])
        cof=ac_dist(instance,kNN,k)
        factors.append(cof)
    return factors