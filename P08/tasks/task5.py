# Evaluate retrieval effectiveness
# ================================

# Task
# ------

# - The ground truth is in `data/cacm.rel`. The format is `queryID Q0 docID rel`
#   where `rel` is 1 if the document is relevant and 0 otherwise.
#   * This file contains only the relevant documents so the value will always be 1.
#     This means that everything that is not in this file counts as non-relevant.
# - Write a script that computes P@5, P@10, Average Precision, and Reciprocal Ranks
#   for each query as well as the averages over the entire query set for the output file generated in Task 4.

# Solution
# --------

from __future__ import division

import math


