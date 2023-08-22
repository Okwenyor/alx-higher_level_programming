#!/usr/bin/python3

import sys

if __name__ == "__main__":
    plus = 0

    for i in range(1, len(sys.argv)):
        plus += int(sys.argv[i])

        print(plus)
