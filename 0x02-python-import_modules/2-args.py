#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv_len = len(sys.argv) - 1
    argv = sys.argv[1:]

    if argv_len == 0:
        print("0 arguments.")
    elif argv_len == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))

    else:
        print("{} arguments:".format(argv_len))
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))
