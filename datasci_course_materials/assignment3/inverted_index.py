import MapReduce
import sys

"""
Inverted Index in the Simple Python MapReduce Framework

Given a set of documents, returns a dictionary where each word is associated
with a list of the document identifiers in which that word appears
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents
    docid = record[0]    # key
    text = record[1]     # value
    words = text.split()
    seen = {}
    for w in words:
        if w not in seen:
            seen[w] = [docid]
            mr.emit_intermediate(w, docid)
        elif docid not in seen[w]:
            seen[w].append(docid)
            mr.emit_intermediate(w, docid)


def reducer(key, list_of_values):
    # key: docid
    # value: a word in that document
    result = []
    for word_list in list_of_values:
        result.extend(word_list)

    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
