# Dmitriy Shin
# December 29, 2019
# Difficulty: Medium

# Description
#   Given an array of ints, return the number of 9's in the array.


def array_count9(arr):
    return arr.count(9)


print(array_count9([1, 2, 9]))  # → 1
print(array_count9([1, 9, 9]))  # → 2
print(array_count9([1, 9, 9, 3, 9]))  # → 3
