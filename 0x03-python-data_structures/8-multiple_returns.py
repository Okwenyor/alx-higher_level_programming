#!/usr/bin/python3
def multiple_returns(sentence):
    v = len(sentence)
    if v == 0:
        initial_value = None
    else:
        initial_value = sentence[0]

    return(v, initial_value)
