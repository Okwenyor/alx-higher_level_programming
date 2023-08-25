#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    total = 0
    old_value = 0

    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    for value in reversed(roman_string):
        result = roman_values.get(value, 0)

        if result >= old_value:
            total += result 

        else:
            total -= result

        old_value = result

    return total


# Test cases
print(roman_to_int("IV"))
print(roman_to_int("CXXIV"))
