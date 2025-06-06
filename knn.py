# -*- coding: utf-8 -*-
"""knn

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g_F2AqRNL6ai70hamO2FUKTrn60phIb7
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

def manhattan_distance(x1, x2):
    return np.sum(np.abs(x1 - x2))

def knn_predict(X_train, y_train, x_test, k, distance_metric=euclidean_distance):
    distances = [distance_metric(x_test, X_train[i]) for i in range(X_train.shape[0])]
    k_nearest_indices = np.argsort(distances)[:k]
    k_nearest_labels = [y_train.iloc[i] for i in k_nearest_indices]
    most_common = np.bincount(k_nearest_labels).argmax()
    return most_common

def knn_classifier(X_train, y_train, X_test, k, distance_metric=euclidean_distance):
    predictions = [knn_predict(X_train, y_train, X_test[i], k, distance_metric) for i in range(X_test.shape[0])]
    return np.array(predictions)