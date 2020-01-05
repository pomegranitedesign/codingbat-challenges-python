# Dmitriy Shin
# January 5, 2020
# make_pi.py
# Description
#   Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

from math import pi


def make_pi():
    return [int(x) for x in str(pi).replace('.', '')][0:3]


print(make_pi())  # → [3, 1, 4]
