# Dmitriy Shin
# December 29, 2019
# Difficulty: Medium

# Description
#   Given a string and a non-negative int n, return a larger string that is n copies of the original string.


def string_times(string, n):
    return string * n


print(string_times('Hi', 2))  # → 'HiHi'
print(string_times('Hi', 3))  # → 'HiHiHi'
print(string_times('Hi', 1))  # → 'Hi'
