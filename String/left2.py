# Dmitriy Shin
# December 29, 2019
# left2.py
# Description
#   Given 2 strings, a and b, return a string of the form short+long+short,
#   with the shorter string on the outside and the longer string on the inside.
#   The strings will not be the same length, but they may be empty (length 0).


def left2(str):
    return str[2:] + str[:2]


print(left2('Hello')) → 'lloHe'
print(left2('java')) → 'vaja'
print(left2('Hi')) → 'Hi'
