# Text preprocessing and document similarity
# ==========================================

# Task
# ----
#   - Create the document-term matrix from Task 2 using scikit-learn
#   - See [this document](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)

# Solution
# --------

from sklearn.feature_extraction.text import CountVectorizer

docs = [
    "The King's Speech",
    "The Lord of the Rings: The Return of the King",
    "Street Kings",
    "The Scorpion King",
    "The Lion King"
]

cv = CountVectorizer()
