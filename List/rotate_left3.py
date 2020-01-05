# Dmitriy Shin
# January 5, 2020
# rotate_left3.py
# Description
#   Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


def rotate_left3(nums):
    copy = [n for n in nums]
    copy[0] = nums[1]
    copy[1] = nums[2]
    copy[2] = nums[0]
    return copy


print(rotate_left3([1, 2, 3]))  # → [2, 3, 1]
print(rotate_left3([5, 11, 9]))  # → [11, 9, 5]
print(rotate_left3([7, 0, 0]))  # → [0, 0, 7]
