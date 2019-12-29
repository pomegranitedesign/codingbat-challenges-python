# Dmitriy Shin
# December 29, 2019
# Difficulty: Medium

# Description
#   Given an array of ints, return True if one of the first 4 elements in the array is a 9.
#   The array length may be less than 4.


def array_front9(arr):
    return arr[0:4].count(9) > 0


print(array_front9([1, 2, 9, 3, 4]))  # → True
print(array_front9([1, 2, 3, 4, 9]))  # → False
print(array_front9([1, 2, 3, 4, 5]))  # → False
