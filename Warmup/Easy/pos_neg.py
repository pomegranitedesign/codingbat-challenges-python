# Dmitriy Shin
# December 29, 2019
# Difficulty: Easy

# Description
#   Given 2 int values, return True if one is negative and one is positive.
#   Except if the parameter "negative" is True, then return True only if both are negative.


def pos_neg(a, b, isNegative):
    return a < 0 and b < 0 if isNegative else ((a < 0 and b > 0) or (a > 0 and b < 0))


print(pos_neg(1, -1, False))  # → True
print(pos_neg(-1, 1, False))  # → True
print(pos_neg(-4, -5, True))  # → True

# NOT PASSED
print(pos_neg(-4, -5, False))  # → False
print(pos_neg(-4, 5, True))  # → False
print(pos_neg(-1, -1, False))  # → False
print(pos_neg(1, -1, True))  # → False
print(pos_neg(-1, 1, True))  # → False
print(pos_neg(-5, -6, False))  # → False
print(pos_neg(-2, -1, False))  # → False
print(pos_neg(-5, 6, True))  # → False
