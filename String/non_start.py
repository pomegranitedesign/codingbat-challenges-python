# Dmitriy Shin
# December 29, 2019
# combo_string.py
# Description
#   Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.


def non_start(a, b):
    return a[1:] + b[1:]


print(non_start('Hello', 'There'))  # → 'ellohere'
print(non_start('java', 'code'))  # → 'avaode'
print(non_start('shotl', 'java'))  # → 'hotlava'
