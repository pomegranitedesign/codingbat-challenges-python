# Dmitriy Shin
# December 31, 2019
# same_first_last.py
# Description
#   Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


def same_first_last(nums):
    return True if len(nums) >= 1 and nums[0] == nums[-1] else False


print(same_first_last([1, 2, 3])) → False
print(same_first_last([1, 2, 3, 1])) → True
print(same_first_last([1, 2, 1])) → True
