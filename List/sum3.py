# Dmitriy Shin
# January 5, 2020
# sum3.py
# Description
#   Given an array of ints length 3, return the sum of all the elements.

from functools import reduce


def sum3(nums):
    return reduce(lambda a, b: a + b, nums)


print(sum3([1, 2, 3]))  # → 6
print(sum3([5, 11, 2]))  # → 18
print(sum3([7, 0, 0]))  # → 7
