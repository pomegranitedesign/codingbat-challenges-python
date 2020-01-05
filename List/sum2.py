# Dmitriy Shin
# January 5, 2020
# sum2.py
# Description
#   Given an array of ints, return the sum of the first 2 elements in the array.
#   If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.


def sum2(nums):
    return nums[0] + nums[1] if len(nums) > 2 else sum(nums)


print(sum2([1, 2, 3]))  # → 3
print(sum2([1, 1]))  # → 2
print(sum2([1, 1, 1, 1]))  # → 2
