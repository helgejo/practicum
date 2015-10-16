# Implement TFIDF retrieval by getting statistics from the Woosh index
# ====================================================================

# Task
# ------

# - Take Task 4 from the last practicum (P07) and update the code such that
#   the term statistics are taken from the Whoosh index

# Solution
# --------

from __future__ import division

import os.path
import math
from collections import Counter

import whoosh.index as index
from whoosh.qparser import QueryParser
from whoosh.fields import Schema, ID, TEXT

index_dir = "../data/index_cacm"
default_field = "content"

# Compute the TFIDF weight of a term
def tfidf(reader, term, count, length):
    tf = count / length
    idf = math.log(reader.doc_count() / reader.doc_frequency(default_field, term))
    return tf*idf

def retrieve_vsm(reader, query):
    # Preprocess the query in a naive way
    qterms = query.split()
    qt = Counter(qterms)

    # Basic algorithm
    # - N is the number of documents
    N = reader.doc_count()
    # score for each doc
    scores = {}
    # normalizer for each doc
    doc_norm = {}
    # normalizer for query
    q_norm = 0
    
    # for each query term t
    for t, cnt in qt.iteritems():
        
        # ignore terms not in the index
        if reader.frequency(default_field, t) == 0:
            print "Query term", t, "ignored"
            continue

        # calculate w_t,q
        wtq = tfidf(reader, t, cnt, len(qterms))
        #print t, wtq
        q_norm += wtq * wtq  # mind that the query normalizer could be ignored
        
        # for each doc in the posting list of t
        pr = reader.postings(default_field, t)
        while pr.is_active():
            docnum = pr.id()  # docnum is the internal (Whoosh) docID
            if docnum not in scores:
                scores[docnum] = 0
                doc_norm[docnum] = 0
            # term freq of t in doc
            freq = pr.value_as("frequency")
            doclen = reader.doc_field_length(docnum, default_field)
            wtd = tfidf(reader, t, freq, doclen)
            scores[docnum] += wtq * wtd
            doc_norm[docnum] += wtd * wtd
            pr.next()
            
    # scores at this points holds the counter of the cosine formula
    # we need to divide by sqrt(q_norm * doc_norm)
    for docnum, score in scores.iteritems():
        scores[docnum] = scores[docnum] / math.sqrt(q_norm * doc_norm[docnum])

    return scores


# Open index
ix = index.open_dir(index_dir)

# Use the reader to get statistics
reader = ix.reader()

query = "algebraic language"

# Retrieve documents using the vector space model
res = retrieve_vsm(reader, query)

for docnum in sorted(res, key=res.get, reverse=True)[:10]:
    # Look up our docID
    stored = reader.stored_fields(docnum)
    print stored['id'], res[docnum]  # doc id and score
    
ix.close()
