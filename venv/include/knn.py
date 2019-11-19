import numpy as np
import math
from scipy.spatial import distance  # compute distances


# create dataset and classes
def createDataSet():
    group = np.array([[4.0, 2.0], [4.2, 2.1], [0.1, 1.4], [0.3, 3.5]])
    label = ['A', 'A', 'B', 'B']
    return group, label


# function KNN
def classify(input, group, label, K):
    input = np.tile(input, (group.shape[0], 1))
    dist = distance.cdist(input, group, 'euclidean')  # Euclidean distances
    # numpy.argsort() sort number from small to big, return indices.
    sortedDistIndex = np.ravel(np.argsort(dist, axis=0))  # np.ravel() compresses dimension

    classCount = {}
    for i in range(K):
        voteLabel = label[sortedDistIndex[i]]  # record classes
        # dic.get(key,default):if has key,get value,else get default
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1

    maxCount = 0
    for k, v in classCount.items():  # extract times
        if v > maxCount:
            maxCount = v
            classes = k
    return classes

group, label = createDataSet()

input=np.array([0.2, 1.5])


K=3
output=classify(input, group, label, K)

print("test data:", input, "classification result:", output)
