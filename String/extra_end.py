# Dmitriy Shin
# December 29, 2019
# extra_end.py
# Description
#   Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
#   The string length will be at least 2.


def extra_end(string=""):
    return string[-2:]*3


print(extra_end('Hello'))  # → 'lololo'
print(extra_end('ab'))  # → 'ababab'
print(extra_end('Hi'))  # → 'HiHiHi'
