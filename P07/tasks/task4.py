# Retrieval using the Vector Space Model
# ======================================

# Task
# ------
#   - Load the index from the disk that was created in Tasks 1 and 2.
#   - Rank documents using keyword queries (e.g., "united states") using the Vector Space Model
#     * Use TF-IDF term weighting and cosine similarity
#   - Display a ranked list of the top 10 matching documents, along with the corresponding relevance scores
#   - Extend `indexer.py` with the necessary methods
#     * Hint: you will need a method that returns the set of documents that contain a given term
#   - Homework: try some of the [different variants for TF and IDF weights](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

# Solution
# --------

from indexer import Index

def retrieve_vsm(index, query):
    # TODO implement retrieval
    pass


# Load index
index = Index()
index.load_from_file("data/index.txt")

query = "united states"
# Retrieve documents using the vector space model
retrieve_vsm(index, query)
