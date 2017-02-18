import MapReduce
import sys

"""
Relational Join Using MapReduce Framework

Returns the same output as the SQL query SELECT * FROM Order, LineItem
    WHERE Order.order_id = LineItem.order_id

Map Input

Each input record is a list of strings representing a tuple in the database.
Each list element corresponds to a different attribute of the table

The first item (index 0) in each record is a string that identifies the table
the record originates from. This field has two possible values:

"line_item" indicates that the record is a line item.
"order" indicates that the record is an order.

The second element (index 1) in each record is the order_id.

LineItem records have 17 attributes including the identifier string.

Order records have 10 elements including the identifier string.
Reduce Output

The output should be a joined record: a single list of length 27 that contains
the attributes from the order record followed by the fields from the line item
record. Each list element should be a string.

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: table
    # value: document contents
    table = record[0]
    attributes = record[1:]
    mr.emit_intermediate(table, attributes)


def reducer(key, list_of_values):
    # key: an order id
    # value: a table
    index = 0
    seen = {}
    for value1 in list_of_values:
        index += 1
        for value2 in list_of_values[index:]:
            if value1[0] == value2[0] and value1[0] not in seen:
                seen[value1[0]] = None
                mr.emit((value1, value2))

# Do not modify below this linej
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
