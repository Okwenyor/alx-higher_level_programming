#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_integers = set()

    for i in my_list:
        if i not in uniq_integers:
            uniq_integers.add(i)
    total_sum = sum(uniq_integers)
    return total_sum
