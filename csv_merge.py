#!/usr/bin/python
# Merge data from the merge spreadsheet into the rows of
# the master spreadsheet using some key columns called merge_cols
#
# All the columns from a matched row in the merge spreadsheet are
# appended to the end of the row in the master spreadsheet. The
# header of the output is also adjusted appropriately.
#

import csv, sys, copy

if len(sys.argv) < 5:
    print "usage: merge_csv.py master merge output merge_cols..."
    sys.exit(1)

master = csv.reader(open(sys.argv[1], 'r'))
merge = csv.reader(open(sys.argv[2], 'r'))
output = csv.writer(open(sys.argv[3], 'w'))

master_indices = []
merge_indices = []
master_header = next(master, None)
merge_header = next(merge, None)
merge_orig = copy.copy(merge_header)

for col in sys.argv[4:]:
    if col in master_header:
        master_indices.append(master_header.index(col))
    else:
        print "could not find col {0} in master header".format(col)

    if col in merge_header:
        merge_indices.append(merge_orig.index(col))
        del(merge_header[merge_header.index(col)])
    else:
        print "could not find col {0} in merge header".format(col)

print "master_indices: {0} with merge_indices: {1}".format(master_indices, merge_indices)

#print merge_header
#print merge_indices

#for index in merge_indices:
#    del(merge_header[index])
#print merge_header
output.writerow(master_header + merge_header)

keys = list()
rows = list()

for row in merge:
    keys.append(tuple([row[index] for index in merge_indices]))
    rows.append(row)

for row in master:
    row_key = tuple([row[index] for index in master_indices])
    if row_key in keys:
        index = keys.index(row_key)
        merge_row = rows[index]
        new_row = []
        for i in xrange(0, len(merge_row)):
            if i not in merge_indices:
                new_row.append(merge_row[i])
        #for index in merge_indices:
        #    del(merge_row[index])

        output.writerow(row + new_row)

