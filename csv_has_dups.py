#!/usr/bin/python3.4
# Checks if a csv has duplicate rows

import sys, csv

if len(sys.argv) == 1:
    print("usage: csv_has_dups.py filename colname")
    sys.exit(1)

reader = csv.reader(open(sys.argv[1], "r"))
header = next(reader)

col_index = header.index(sys.argv[2])

entry_set = set()
duplicate_rows = dict()
row_num = 2

for row in reader:
    entry = row[col_index]
    if (entry in entry_set):
        if entry in duplicate_rows:
            duplicate_rows[entry] += [row_num]
        else:
            duplicate_rows[entry] = [row_num]
    else:
        entry_set.add(entry)

    row_num += 1

for key, value in duplicate_rows.items():
    print("Duplicate report:")
    print("[{0}]: {1}".format(key, value))
