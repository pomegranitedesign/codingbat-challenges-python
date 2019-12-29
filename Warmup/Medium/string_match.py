# Dmitriy Shin
# December 29, 2019
# Difficulty: Medium

# Description
#   Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
#   So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


def string_match(a, b):
    left_side = split_by_two(a)
    right_side = split_by_two(b)
    count = 0

    for i, j in zip(left_side, right_side):
        if i == j:
            count += 1
    return count


def split_by_two(string):
    return [string[i:i+2] for i in range(0, len(string) - 1)]


print(string_match('xxcaazz', 'xxbaaz'))  # → 3
print(string_match('abc', 'abc'))  # → 2
print(string_match('abc', 'axc'))  # → 0
