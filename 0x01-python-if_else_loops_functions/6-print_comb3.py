#!/usr/bin/python3
for i in range(10):
    for v in range(i+1, 10):
        if i == 8 and v == 9:
            print('89')
        else:
            print('{:d}{:d}, ' .format(i, v), end='')
