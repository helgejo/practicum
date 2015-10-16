# Implement TFIDF retrieval by getting statistics from the Woosh index
# ====================================================================

# Task
# ------

# - Take Task 4 from the last practicum (P07) and update the code such that
#   the term statistics are taken from the Whoosh index we built in Task 2

# Solution
# --------

from __future__ import division

import os.path
import whoosh.index as index
from whoosh.fields import Schema, ID, TEXT

index_dir = "../data/index_cacm"


# Compute the TFIDF weight of a term
def tfidf(index, term, count, length):
    tf = count / length
    idf = math.log(index.num_docs() / len(index.get_postings(term)))
    return tf*idf

def retrieve_vsm(index, query):
    # Preprocess the query (the same way as we preprocesssed documents)
    qterms = parse(query)
    qt = Counter(qterms)

    # Basic algorithm
    # - N is the number of documents
    N = index.num_docs()  # TODO update
    # score for each doc
    scores = {}
    # normalizer for each doc
    doc_norm = {}
    # normalizer for query
    q_norm = 0
    
    # for each query term t
    for t, cnt in qt.iteritems():
        postings = index.get_postings(t) # TODO update
        # ignore terms not in the index
        if postings is None:
            continue

        # calculate w_t,q
        wtq = tfidf(index, t, cnt, len(qterms))
        print t, wtq
        q_norm += wtq * wtq
        
        # for each doc in the posting list of t
        for p in postings:
            doc_id = p.doc_id
            if doc_id not in scores:
                scores[doc_id] = 0
                doc_norm[doc_id] = 0
            # term freq of t in doc
            freq = int(p.payload)  # TODO update
            doclen = index.get_doc_meta(doc_id)['length']  # TODO update
            wtd = tfidf(index, t, freq, doclen)
            scores[doc_id] += wtq * wtd
            doc_norm[doc_id] += wtd * wtd
            
    # scores at this points holds the counter of the cosine formula
    # we need to divide by sqrt(q_norm * doc_norm)
    for doc_id, score in scores.iteritems():
        scores[doc_id] = scores[doc_id] / math.sqrt(q_norm * doc_norm[doc_id])

    return scores


# Open index
ix = index.open_dir(index_dir)

# Use the reader to get statistics
reader = ix.reader()

query = "algebraic language"

# Retrieve documents using the vector space model
res = retrieve_vsm(index, query)

for doc_id in sorted(res, key=res.get, reverse=True)[:10]:
    print res[doc_id]
    
ix.close()
