Practicum 2
===========

Learning objectives:

  - Loading small data sets
  - Computing summary statistics (mean, median, range, variance, etc.)
  - Visualization
  - Setting up local environment
  

## Task 1. Computing summary statistics on the Iris dataset
 
  - Load the Iris dataset (`data/iris.data`)
  - Answer the following questions:
    * What is the mean `sepal length` for Iris Setosa?
    * What is the median `petal length` for Iris Virginica?
    * What is the range of `sepal width` for Iris Versicolour?
    * Which class (Setosa/Versicolour/Virginica) shows the highest variance in `petal width`?
    * What is the 70% percentile for `sepal length` and `sepal width` (for all classes together)?
    * Compute Absolute Average Deviation (AAD), Median Absolute Deviation (MAD), and Interquartile Range (IQR) for `petal length` (for all classes together).
  
  
## Task 2. Computing summary statistics using numpy

  - Load the Iris dataset into a 150x4 numpy array.
  - Answer the questions from Task 1 (except the last one) using numpy.
  - See reference at the bottom of the document.


## References

  - [Numpy arrays](http://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array)
  - [Numpy statistics](http://docs.scipy.org/doc/numpy/reference/routines.statistics.html)
    