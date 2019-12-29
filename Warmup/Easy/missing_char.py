# Dmitriy Shin
# December 29, 2019
# Difficulty: Easy

# Given a non-empty string and an int n, return a new string where the char at index n has been removed.
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).


def missing_char(string, n):
    return string.replace(string[n], "")


print(missing_char('kitten', 1))  # → 'ktten'
print(missing_char('kitten', 0))  # → 'itten'
print(missing_char('kitten', 4))  # → 'kittn'
