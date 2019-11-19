import numpy as np
from math import sqrt
from collections import Counter

import urllib.request
import requests



def feature_label(k, X_train, Y_train, x):
    if k <= 1:
        print('Please check the number of neighbours!')
        return -1
    elif k == len(Y_train):
        return -1
    else:
        label = [sqrt(np.sum((x_train - x)**2)) for x_train in X_train]
        nearest = np.argsort(label)
        topk_y = [Y_train[i] for i in nearest[:k]]
        votes = Counter(topk_y)
        if votes:
            return votes.most_common(1)[0][0]
        else:
            return -1

if __name__ == "__main__":
    outcome = 0
    URLs = "https://dwo0tbj14j3pa.cloudfront.net/records/all"
    r = requests.get(url = URLs)
    data = r.json()
    print(data[-1])
    X_train = np.array([[1.0, 3.5], [2.0, 7], [3.0, 12], [4.0, 14], [5, 28], [6, 30], [7, 35], [8, 40], [9, 9], [11, 11], [12, 12], [14, 14]])
    Y_train = np.array(['low', 'low', 'low', 'low', 'mid', 'mid', 'mid', 'mid', 'high', 'high', 'high', 'high'])
    x = np.array([10, 10])
    label = feature_label(3, X_train, Y_train, x)
    if label == -1:
        print('There is an error in the system, please check')
    else:
        outcome = label
        print("The label is:", label)