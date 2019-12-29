# Dmitriy Shin
# December 29, 2019
# Difficulty: Easy

# Description
#   Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


def diff21(n):
    return (n - 21)*2 if n > 21 else 21 - n


print(diff21(19))  # → 2
print(diff21(10))  # → 11
print(diff21(21))  # → 0
