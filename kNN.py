#!/usr/bin/env python

import numpy as np


def knn(in_x, train_set, labels, k):
    """
    Args:
        in_x (Optional[int]): input data
        train_set (np.array): train set
        labels (Optional[str]): labels of train set
        k (int): select k more mini distances to evaluate

    """
    train_len = train_set.shape[0]
    diff_mat = np.tile(in_x, (train_len, 1)) - train_set  # type: np.array
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_distances = distances.argsort()
    class_count = {}
    for i in xrange(k):
        vote_label = labels[sorted_distances[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(
        class_count.items(), lambda x, y: cmp(y[1], x[1]))
    return sorted_class_count[0][0]


if __name__ == '__main__':
    m_train_set = np.array(
        [[3, 4], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    m_labels = np.array(['love', 'love', 'love', 'action', 'action', 'action'])
    print knn([98, 9], m_train_set, m_labels, 3)
