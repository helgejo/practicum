Practicum 4
===========

Learning objectives:

  - Introduction to scikit-learn
  - Using and comparing various classification algorithms in scikit-learn
  - Working on Assignment 1
  

## Task 0. Scikit-learn introduction

  - Different machine learning tasks
  - Loading example datasets
  

## Task 1. Running a decision tree classifier on the Iris dataset
 
  - Divide the Iris dataset to 2/3 training and 1/3 test sets
  - Train a decision tree classifier and apply it on the test data
  - See [this document](http://scikit-learn.org/stable/modules/tree.html#tree-classification) for help
  - Evaluate the predictions: compute accuracy and error rate

  
## Task 2. Comparing different classifiers on the Iris dataset

  - Using the previous 2/3-1/3 splits, train different classifiers and compare their performance by filling in the following table:

| Method            | Accuracy | Error rate |
| ----------------- | -------- | ---------- |
| Decision tree     |          |            |
| Nearest Neighbors |          |            |
| Naive Bayes       |          |            |
| SVM               |          |            |
| Random Forest     |          |            |

  - Documentation for the classifiers can be found here:
    * [Decision trees](http://scikit-learn.org/stable/modules/tree.html)
    * [Nearest Neighbors](http://scikit-learn.org/stable/modules/neighbors.html)
    * [Naive Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html)
    * [SVM](http://scikit-learn.org/stable/modules/svm.html)
    * [Random Forest](http://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees)
  

## Task 3. Performing classification on the Cylinder Bands dataset

  - Download the Cylinder Bands dataset from the mldata.org repository
    * See [this document](http://scikit-learn.org/stable/datasets/index.html#downloading-datasets-from-the-mldata-org-repository) for help
    * [Cylinder Bands dataset on mldata.org](http://mldata.org/repository/data/viewslug/uci-20070111-cylinder-bands/)
  - Train a classifier (any classifier) and evaluate its performance using cross-validation
    * See [this document](http://scikit-learn.org/stable/modules/cross_validation.html) for help
  

## Task 4. Comparing two classifiers on the Cylinder Bands dataset

  - Divide the Cylinder Bands dataset into 80% training and 20% test sets randomly
  - Compare the performance of two classifiers by increasing the amount of training data incrementally
  - Plot performance as a function of training data available


## Task 5. Working on Assignment 1

  
## References

  - Scikit-learn
    * [Tutorial](http://scikit-learn.org/stable/tutorial/index.html)
    * [Supervised learning](http://scikit-learn.org/stable/supervised_learning.html)
    * [Class and function reference](http://scikit-learn.org/stable/modules/classes.html)
    * [Dataset loading utilities](http://scikit-learn.org/stable/datasets/index.html)
  - [Scikit-learn tutorial video](https://vimeo.com/53062607) and [online material](http://www.astroml.org/sklearn_tutorial/)
  