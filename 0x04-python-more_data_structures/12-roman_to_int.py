#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
            }
    arabic_numeral = 0
    prev_value = 0

    for c in reversed(roman_string):
        if c not in roman_numerals:
            return 0

        value = roman_numerals[c]
        if value >= prev_value:
            arabic_numeral += value
        else:
            arabic_numeral -= value
        prev_value = value

    return arabic_numeral
