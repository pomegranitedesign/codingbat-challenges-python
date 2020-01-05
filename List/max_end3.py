# Dmitriy Shin
# January 5, 2020
# max_end3.py
# Description
#   Given an array of ints length 3, figure out which is larger, the first or last element in the array, \
#   and set all the other elements to be that value. Return the changed array.


def max_end3(nums):
    del nums[1]
    return [max(nums) for _ in range(3)]


print(max_end3([1, 2, 3]))  # → [3, 3, 3]
print(max_end3([11, 5, 9]))  # → [11, 11, 11]
print(max_end3([2, 11, 3]))  # → [3, 3, 3]
