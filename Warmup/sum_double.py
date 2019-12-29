# Dmitriy Shin
# December 29, 2019
# Difficulty: Easy

# Description
#   Given two int values, return their sum. Unless the two values are the same, then return double their sum.


def sum_double(a=0, b=0):
    return (a+b)*2 if a == b else a + b


print(sum_double(1, 2))  # → 3
print(sum_double(3, 2))  # → 5
print(sum_double(2, 2))  # → 8
