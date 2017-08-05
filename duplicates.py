from collections import Counter
import os
from os.path import (
            basename,
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
            fpathes_sized[fpath] = fsize
            fsizes.append(fsize)
    size_counter = Counter(fsizes)
    fnames_counter = Counter(fnames)
    for fpath, fsize in fpathes_sized.items():
        if fnames_counter[basename(fpath)] > 1 and size_counter[fsize] > 1:
            file_duplicates[fpath] = fsize
    return file_duplicates


if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print('\nEnter: python3 duplicates.py "dirpath"\n')
    dirpath = sys.argv[1]
    file_duplicates = find_file_duplicates(dirpath)
    for fpath, fsize in file_duplicates.items():
        print("{} : {}".format(fpath, fsize))
