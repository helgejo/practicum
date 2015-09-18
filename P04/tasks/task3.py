# Performing classification on the Cylinder Bands dataset
# =======================================================

# Task
# ----
#   - Download the Cylinder Bands dataset from the mldata.org repository
#     * See [this document](http://scikit-learn.org/stable/datasets/index.html#downloading-datasets-from-the-mldata-org-repository) for help
#     * [Cylinder Bands dataset on mldata.org](http://mldata.org/repository/data/viewslug/uci-20070111-cylinder-bands/)
#   - Train a classifier (any classifier) and evaluate its performance using cross-validation
#     * See [this document](http://scikit-learn.org/stable/modules/cross_validation.html) for help

# Solution
# --------

from __future__ import division

import csv

from sklearn.datasets import fetch_mldata

# load using mldata loader (should work locally)
# cylinder = fetch_mldata('uci-20070111-cylinder-bands')

# load CSV
filename = "../data/uci-20070111-cylinder-bands.csv"
data_x = []
data_y = []
with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            data_x.append(row[:-1])  # 1..n-1 are the attributes
            data_y.append(row[-1])  # last element is the class label

# TODO build model

# TODO cross-validation
