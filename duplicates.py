from collections import Counter
import operator
import os
from os.path import (
            dirname,
            join,
            getsize,
            )
import sys


def find_file_duplicates(dirpath):
    file_duplicates = {}
    fpathes_sized = {}
    fsizes = []
    fnames = []
    for root, dirs, files in os.walk(dirpath):
        fnames.extend(files)
        for fname in files:
            fpath = join(root, fname)
            fsize = getsize(fpath)
            # (fname, fsize) can't be the key because of possible duplicates
            fpathes_sized[fpath] = (fname, fsize)
            fsizes.append(fsize)
    size_counter = Counter(fsizes)
    fnames_counter = Counter(fnames)
    for fpath, (fname, fsize) in fpathes_sized.items():
        if fnames_counter[fname] > 1 and size_counter[fsize] > 1:
            file_duplicates[fpath] = fname
    return file_duplicates


def output_file_duplicates_to_console(file_duplicates, second_item=1):
    print('\nFound next file duplicates in {}:\n'.format(dirpath))
    for (fpath, fname) in sorted(
                            file_duplicates.items(),
                            key=operator.itemgetter(second_item)
                            ):
        print("{} ---> {}".format(fname, dirname(fpath)))
    print()


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print('\nEnter: python3 duplicates.py "dirpath"\n')
        sys.exit()
    dirpath = sys.argv[1]
    if not os.path.exists(dirpath):
        print('\nThis dirpath does not exist\n')
        sys.exit()
    file_duplicates = find_file_duplicates(dirpath)
    if not file_duplicates:
        print('\nThere is no any file duplicates\n')
    output_file_duplicates_to_console(file_duplicates)
