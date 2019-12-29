# Dmitriy Shin
# December 29, 2019
# Difficulty: Easy

# Description
# Given an int n, return True if it is within 10 of 100 or 200.
# Note: abs(num) computes the absolute value of a number.


def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


print(near_hundred(93))  # → True
print(near_hundred(90))  # → True
print(near_hundred(89))  # → False
