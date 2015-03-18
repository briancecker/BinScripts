#!/usr/bin/python3
from optparse import OptionParser
from functools import reduce
from random import shuffle
import sys

def get_opts():
    parser = OptionParser()
    parser.add_option("-r", "--train", dest="train_split", action="store",
            help="Required: Training split as a percentage (70%) or number (70)")
    parser.add_option("-t", "--test", dest="test_split", action="store",
            help="Required: Testing split as a percentage (30%) or number (30)")
    parser.add_option("-d", "--dev", dest="dev_split", action="store",
            help="Dev split as a percentage (30%) or number (30)")
    parser.add_option("-f", "--file", dest="file", action="store",
            help="Input file to sample")
    parser.add_option("--has-header", dest="has_header", action="store_true",
            help="File has a header to skip")

    (options, args) = parser.parse_args()

    if (options.train_split is None or options.test_split is None
                or options.file is None):
            parser.print_help()
            sys.exit(1)

    split_nums = list(filter(lambda x: x is not None,
            [options.train_split, options.test_split, options.dev_split]))

    if (len(set(map(lambda x: "p" if "%" in x else "i", split_nums))) != 1):
        # Not all the same type of item (all ints or all percentages)
        print("error: training, test, and dev splits need to be all ints or all percentages")
        sys.exit(1)

    using_percentages = True in [("%" in x) for x in split_nums]
    if (using_percentages):
        # using percentages, check that they sum to 100
        if (reduce(lambda acc, x: acc + x,
                map(lambda x: int(x.replace("%", "")), split_nums)) != 100):
            print("Split percentages don't sum to 100!")
            sys.exit(1)

    return (using_percentages, options, args)

def split_num_to_int(num):
    return None if num is None else int(num.replace("%", ""))

def take_percentage(lines, perc):
    return 0 if perc is None else round(len(lines) * float(perc) / 100)

def to_file(in_filename, header, lines, ext):
    if len(lines) == 0:
        return
    orig_ext = in_filename[in_filename.index("."):]
    out_file = "splits/" + in_filename[:in_filename.index(".")] + ext + orig_ext
    with open(out_file, 'w') as f:
        if header:
            f.write(header)
        f.writelines(lines)

def run():
    (using_percentages, options, args) = get_opts()
    with open(options.file, 'r') as f:
        lines = [line for line in f]
        header = None
        shuffle(lines)
        if options.has_header:
            header = lines[0]
            lines = lines[1:]
        tr_num = split_num_to_int(options.train_split)
        d_num = split_num_to_int(options.dev_split)
        t_num = split_num_to_int(options.test_split)
        if (using_percentages):
            tr_num = take_percentage(lines, tr_num)
            d_num = take_percentage(lines, d_num)
            t_num = take_percentage(lines, t_num)

        print("Taking {0} for training, {1} for testing, and {2} for dev"
                .format(tr_num, t_num, d_num))

        train = lines[0:tr_num]
        test = lines[tr_num:tr_num+t_num]
        dev = lines[tr_num+t_num:]

        to_file(options.file, header, train, ".train")
        to_file(options.file, header, test, ".test")
        to_file(options.file, header, dev, ".dev")

if __name__ == "__main__":
    run()
