# Comparing different classifiers on the Iris dataset
# ===================================================

# Task
# ----
#   - Using the previous 2/3-1/3 splits, train different classifiers and compare their performance
#     by filling in the following table:
#
# | Method            | Accuracy | Error rate |
# | ----------------- | -------- | ---------- |
# | Decision tree     | 0.86     | 0.14       |
# | Nearest Neighbors |          |            |
# | Naive Bayes       |          |            |
# | SVM               |          |            |
# | Random Forest     |          |            |
#
#   - Documentation for the classifiers can be found here:
#     * [Decision trees](http://scikit-learn.org/stable/modules/tree.html)
#     * [Nearest Neighbors](http://scikit-learn.org/stable/modules/neighbors.html)
#     * [Naive Bayes](http://scikit-learn.org/stable/modules/naive_bayes.html)
#     * [SVM](http://scikit-learn.org/stable/modules/svm.html)
#     * [Random Forest](http://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees)

# Solution
# --------

from __future__ import division

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier

# ### Evaluating predictions
# This function evaluates the predictions by comparing them to the true labels
def evaluate(predictions, true_labels):
    correct = 0
    incorrect = 0
    for i in range(len(predictions)):
        if predictions[i] == true_labels[i]:
            correct += 1
        else:
            incorrect += 1

    print "Accuracy:   ", correct / len(predictions)
    print "Error rate: ", incorrect / len(predictions)
    
    return 0


# import some data to play with
iris = datasets.load_iris()

# ### Split the data into training and test sets
# (we don't do a random split so that we have the same splits for all experiments)
train_x = []  # train attributes
train_y = []  # train class labels
test_x = []  # test attributes
test_y = []  # test class labels

for i in range(len(iris.data)):
    if i % 3 == 0:  # test instance
        test_x.append(iris.data[i])
        test_y.append(iris.target[i])
    else:  # train instance
        train_x.append(iris.data[i])
        train_y.append(iris.target[i])

# ### Create a decision tree classifier object
clf = DecisionTreeClassifier()

# ### Train the classifier
clf.fit(train_x, train_y)

# ### Apply it to the test data
predictions = clf.predict(test_x)

# ### Evaluate the predictions
evaluate(predictions, test_y)

