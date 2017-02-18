import MapReduce
import sys

"""
Asymmetric Friends in the Simple Python MapReduce Framework

Given an input record as a 2-element list [personA, personB], returns the
list of all one-way friendships, i.e. personA is friends with personB, but
personB is not friends with personA
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
    mr.emit_intermediate(friend, person)


def reducer(key, list_of_values):
    # key: person
    # value: list of friends
    for friend in list_of_values:
        if list_of_values.count(friend) < 2:
            mr.emit((key, friend))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
