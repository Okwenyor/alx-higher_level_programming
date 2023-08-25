#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    total = 0
    prev_value = 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}

    for char in reversed(roman_string):
        value = roman_values[char]
        result = roman_values.get(value, 0)

        if result >= prev_value:
            total += value

        else:
            total -= value
            prev_value = value

    return total
