Practicum 1
===========

Learning objectives:

  - Familiarize with the programming environment (Python and DataJoy)
  - Variable transformation (normalization, binarization, discretization)
  - Proximity calculations
  - Simple plotting


See the document on itslearning about the programming environment, etc.
You will need to register on getdatajoy.com to access the solutions documents 
with explanations and output, generated automatically from the source files.
  

## Task 1. Variable transformation: normalization by scaling between 0 and 1
 
  - Generate a random value that is the sum of rolling two six-sided dice.
  - Create a vector with n random values.
  - Plot the distribution of the values on a histogram.
  - Normalize the values between 0 and 1 using Min-Max normalization.
  - Plot the distribution of the normalized values on a histogram.


## Task 2. Computing the similarity of binary vectors

  - Create a binary representation of the records that have nominal and ordinal attributes.
  - Implement the functions that compute the Simple Matching Coefficient and Jaccard Coefficient for a given pair of records.
  - Find the most similar pair of records according to each similarity measure.


## Task 3. Computing similarity between documents

  - Compute the similarity between two documents.
  - Represent each document as a vector of binary attributes: if a given word is present in the document or not.
  - You can then use the Jaccard coefficient.


## References

  - [Matplotlib plotting framework](http://matplotlib.org/api/pyplot_api.html)
    