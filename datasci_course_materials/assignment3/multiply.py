import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework

Given two matrices, in a sparse matrix format with records of the form (matrix
id, i, j, value) where matrix id is either 'a' or 'b' returns the result of
multiplying the matrices as a series of tuples of the form (i, j, value)
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: matrix id
    # value: (i, j, value)
    matrix_id = record[0]
    i, j, value = record[1:]
    if matrix_id == 'a':
        mr.emit_intermediate(i, (j, value, 'a'))
    else:
        mr.emit_intermediate(j, (i, value, 'b'))


def reducer(key, list_of_values):
    # key: row id from 'a' or col id from 'b'
    # value: (i, value, matrix_id)
    matrix_a_tuples = filter(lambda x: 'a' in x, list_of_values)
    matrix_b_tuples = filter(lambda x: 'b' in x, list_of_values)

    for tuple_a in matrix_a_tuples:
        i = tuple_a[0]
        value_a = tuple_a[1]
        products = []
        j = 0
        for tuple_b in matrix_b_tuples:
            value_b = tuple_b[1]
            products.append(value_a * value_b)

        j += 1
        mr.emit((i, j, sum(products)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
