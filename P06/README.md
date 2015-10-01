Practicum 6
===========

Learning objectives:

  - Using clustering algorithms in scikit-learn
  

## Task 1. Perform K-Means clustering using scikit-learn

  - A set of 2D data points are given (generated artificially)
  - Perform K-means clustering using scikit-learn using the following two configurations:
    * K=3, 10 iterations, and random centroid selection
    * K=6, 3 iterations, and providing the initial centroids manually
  - Visualize the resulting clusters and the cluster centroids
  - See [this document](scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) for help


## Task 2. Text preprocessing and document similarity

  - Write a function that creates (and prints out) the document-term matrix from an input set of documents
  - Apply the following preprocessing steps:
    * Tokenization
    * Lowercasing
    * Stopword removal
    * Suffix-s stemming
  - Implement a function that computes the cosine similarity of two term vectors
  
  

## References

  - [Clustering in scikit-learn](http://scikit-learn.org/stable/modules/clustering.html)
    