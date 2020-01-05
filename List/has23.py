# Dmitriy Shin
# January 5, 2020
# has23.py
# Description
#   Given an int array length 2, return True if it contains a 2 or a 3.


def has23(nums):
    return 2 in nums or 3 in nums


print(has23([2, 5]))  # → True
print(has23([4, 3]))  # → True
print(has23([4, 5]))  # → False
