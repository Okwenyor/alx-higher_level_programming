#!/usr/bin/python3

a = 10
b = 5

if __name__ == '__main__":
    from calculator_1 import add, sub, mul, div

    addition_result = add(a, b)
    subtraction_result = sub(a, b)
    division_result = div(a, b)
    multiplication_result = mul(a, b)

    print("{} + {} = {}".format(a, b, addition_result))
    print("{} - {} = {}".format(a, b, subtraction_result))
    print("{} / {} = {}".format(a, b, division_result))
    print("{} * {} = {}".format(a, b, multiplication_result))
