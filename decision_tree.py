#!/usr/bin/env python

import numpy as np


def calc_shannon_ent(data_set):
    data_set_len = len(data_set)
    label_counts = {}
    for item in data_set:
        current_label = item[-1]
        label_counts[current_label] = label_counts.get(current_label, 0) + 1
    label_prob = np.array(label_counts.values()) / float(data_set_len)
    shannon_ent = - (np.log2(label_prob) * label_prob).sum()
    return shannon_ent


def split_shannon_ent(data_set, axis, value):
    result_data_set = []
    for item in data_set:
        if item[axis] == value:
            reduce_feature = item[:axis] + item[axis + 1:]
            result_data_set.append(reduce_feature)
    return result_data_set


def choose_best_feature(data_set):
    num_features = len(data_set[0]) - 1
    len_set = len(data_set)
    base_shannon_ent = calc_shannon_ent(data_set)
    best_gain_info = -1.0
    best_feature_index = -1.0
    for i in xrange(num_features):
        split_ent = 0
        feature_values = [item[i] for item in data_set]
        for val in feature_values:
            split_shannon_set = split_shannon_ent(data_set, i, val)
            pro = len(split_shannon_set) / float(len_set)
            split_ent += calc_shannon_ent(split_shannon_set) * pro
        gain_info = base_shannon_ent - split_ent
        if gain_info > best_gain_info:
            best_gain_info = gain_info
            best_feature_index = i
    return best_feature_index


class Node(object):
    def __init__(self, label, status):
        self.label = label
        self.status = status
        self.next_nodes = []


def majority_class(class_list):
    class_count = {}
    for item in class_list:
        class_count[item] = class_count.get(item, 0) + 1
    class_count_sorted = sorted(class_count.items(), lambda x, y: cmp(y[1], x[1]))
    return class_count_sorted[0][0]


def create_tree(data_set, labels, pre_status='root'):
    class_list = [item[-1] for item in data_set]
    if class_list.count(class_list[0]) == len(class_list):
        node = Node(class_list[0], pre_status)
        return node
    if len(data_set[0]) == 1:
        node = Node(majority_class(class_list))
        return node
    best_feature = choose_best_feature(data_set)
    feature_values = [item[best_feature] for item in data_set]
    root = Node(labels[best_feature], pre_status)
    del labels[best_feature]
    for val in feature_values:
        sub_labels = labels[:]
        split_data_set = split_shannon_ent(data_set, best_feature, val)
        root.next_nodes.append(create_tree(split_data_set, sub_labels, val))
    return root


def create_data_set():
    data_set = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ]
    labels = ['no surfacing', 'flippers']
    return data_set, labels


if __name__ == '__main__':
    m_data, m_labels = create_data_set()
    # print calc_shannon_ent(m_data)
    # print split_shannon_ent(m_data, 0, 1)
    # print choose_best_feature(m_data)
    root_tree = create_tree(m_data, m_labels)
