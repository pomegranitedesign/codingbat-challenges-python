# Dmitriy Shin
# December 29, 2019
# Difficulty: Easy

# Description
# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


def makes10(a, b):
    return a == 10 or b == 10 or (a + b) == 10


print(makes10(9, 10))  # → True
print(makes10(9, 9))  # → False
print(makes10(1, 9))  # → True
