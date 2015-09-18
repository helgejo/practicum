# Running a decision tree classifier on the Iris dataset
# ======================================================

# Task
# ----
#   - Divide the Iris dataset to 2/3 training and 1/3 test sets
#   - Train a decision tree classifier and apply it on the test data
#   - Evaluate the predictions: compute accuracy and error rate

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
