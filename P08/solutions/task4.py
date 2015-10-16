# Generate retrieval results in "batch mode"
# ==========================================

# Task
# ------

# - Using the retrieval algorithm from Task 3, process the queries in `data/cacm.query.xml`
#   and output the top 10 results to a single file, `data/cacm.out`,
#   in the following format (one result per line) `queryID Q0 docID score`

# Solution
# --------

from __future__ import division

import math
from collections import Counter
import whoosh.index as index

# For parsing the XML file
from xml.dom import minidom


index_dir = "../data/index_cacm"
query_file = "../data/cacm.query.xml"
output_file = "../data/cacm.out"
default_field = "content"


# Load queries from the query xml file
def load_queries():
    queries = []
    xmldoc = minidom.parse(query_file)
    for query in xmldoc.getElementsByTagName("query"):
        query_id = query.getElementsByTagName("number")[0].firstChild.nodeValue
        text = query.getElementsByTagName("text")[0].firstChild.nodeValue
        queries.append({'id': query_id, 'text': text})

    return queries

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
            #print "Query term", t, "ignored"
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

queries = load_queries()

outfile = open(output_file, "w")

for query in queries:
    print "Processing query number", query['id']

    # Retrieve documents using the vector space model
    res = retrieve_vsm(reader, query['text'])

    # Output max 10 results
    for docnum in sorted(res, key=res.get, reverse=True)[:10]:
        # Look up our docID
        stored = reader.stored_fields(docnum)
        # Write `docID Q0 queryID score` into `data/cacm.out`
        outfile.write(stored['id'] + " Q0 " + query['id'] + " " + str(res[docnum]) + "\n")

outfile.close()
ix.close()
