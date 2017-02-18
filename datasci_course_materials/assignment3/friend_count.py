import MapReduce
import sys

"""
Friend Count in the Simple Python MapReduce Framework

Given an input record as a 2-element list [personA, personB], returns the
number of friends each person has
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: person
    # value: friend
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)


def reducer(key, list_of_values):
    # key: person
    # value: list of friends
    mr.emit((key, len(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
