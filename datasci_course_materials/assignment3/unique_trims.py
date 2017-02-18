import MapReduce
import sys

"""
Unique Trims in the Simple Python MapReduce Framework

Given an input record as a 2-element list [sequence id, nucleotide sequence],
returns each sequence after removing the last 10 nucleotides
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: sequence_id
    # value: nucleotides
    seq_id = record[0]
    nucleotides = record[1]
    mr.emit_intermediate(seq_id, nucleotides[:-10])


def reducer(key, list_of_values):
    # key: sequence_id
    # value: nucleotides
    mr.emit(list_of_values[0])

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
