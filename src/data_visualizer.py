import numpy as np
from sklearn import decomposition
from matplotlib import pyplot as plt

from dataset_io import read_csv
from transform_data import z_score

def reduce_with_pca(data):

  pca = decomposition.PCA(n_components=2)
  pca.fit(data)

  return pca.fit_transform(data)

def plot_2d_data(data, labels):
  markers = ('s', 'd', 'o')
  colors = {0: 'yellow', 1: 'blue', 2: 'lightgreen', 3: 'orange'}

  #plt.scatter(data[:, 0], data[:, 1],
  #            marker=markers(labels[:]),
  #            c=colors(labels[:])
  plt.figure()
  for idx, row in enumerate(data):
    plt.scatter(row[0], row[1],
                c=colors.get(labels[idx], 'red'),
                marker='o')
  plt.show()
