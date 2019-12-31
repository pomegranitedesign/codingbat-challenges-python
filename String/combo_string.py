# Dmitriy Shin
# December 29, 2019
# combo_string.py
# Description
#   Given 2 strings, a and b, return a string of the form short+long+short,
#   with the shorter string on the outside and the longer string on the inside.
#   The strings will not be the same length, but they may be empty (length 0).


def combo_string(a, b):
    return (a + b + a) if len(a) < len(b) else (b + a + b)


print(combo_string('Hello', 'hi'))  # → 'hiHellohi'
print(combo_string('hi', 'Hello'))  # → 'hiHellohi'
print(combo_string('aaa', 'b'))  # → 'baaab'
