#!/usr/bin/python3
# Removes all rows in csv1 that are in csv2 by key_cols
# and writes to csv_out
#

import csv, sys

if len(sys.argv) < 4:
    print("usage: csv_exclude.py csv1 csv2 csv_out key_cols...")
    print("Removes all rows in csv1 that are in csv2 by key_cols and writes to csv_out")

csv1 = csv.reader(open(sys.argv[1], "r"))
csv1_head = next(csv1)
csv1_indices = list()
csv2 = csv.reader(open(sys.argv[2], "r"))
csv2_head = next(csv2)
csv2_indices = list()
csv_out = csv.writer(open(sys.argv[3], "w"))

for col in sys.argv[4:]:
    if col not in csv1_head or col not in csv2_head:
        print("could not find col {0} in one of the input headers")
    else:
        csv1_indices.append(csv1_head.index(col))
        csv2_indices.append(csv2_head.index(col))

csv_out.writerow(csv1_head)

keys = list()
rows = list()

for row in csv2:
    keys.append(tuple([row[index] for index in csv2_indices]))

for row in csv1:
    row_key = tuple([row[index] for index in csv1_indices])
    if row_key not in keys:
        csv_out.writerow(row)

