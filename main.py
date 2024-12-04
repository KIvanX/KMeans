import random
import time

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score


def silhouette_method():
    sse = []
    for k in range(2, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit_predict(data)
        sse.append(silhouette_score(data, kmeans.labels_))
    plt.plot(range(2, 11), sse, marker='o')
    plt.title('Метод "Силуэтов"')
    plt.xlabel('Количество кластеров')
    plt.ylabel('Оценка метода')
    plt.show()


def my_k_means(points, k):
    centers = [points[i] for i in range(k)]
    prev_res = 0
    while True:
        res = 0
        summator = [[0] * len(points[0]) for _ in range(k)]
        p_class = [0 for _ in range(len(data))]
        for p_i, point in enumerate(points):
            lens = [sum([(c - p) ** 2 for c, p in zip(centers[i], point)]) ** 0.5 for i in range(len(centers))]
            ind = lens.index(min(lens))
            summator[ind] = [c + p for c, p in zip(summator[ind], point)]
            p_class[p_i] = ind
            res += min(lens)

        centers = [[d / p_class.count(i) for d in summator[i]] for i in range(k)]

        show_results(p_class, centers)

        if abs(res - prev_res) < 10**-3:
            return p_class
        prev_res = res


def show_results(colors, centroids):
    fig, ax = plt.subplots(4, 4)
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            ax[i][j].scatter(data[:, i], data[:, j], c=colors)
            ax[i][j].scatter([centroid[i] for centroid in centroids],
                             [centroid[j] for centroid in centroids], c='red', marker='x')
    plt.show()
    time.sleep(1)


dataset = load_iris()
data = dataset['data']

my_k_means([(d[0], d[1], d[2], d[3]) for d in data], 3)
