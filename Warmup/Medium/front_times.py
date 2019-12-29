# Dmitriy Shin
# December 29, 2019
# Difficulty: Medium

# Description
#   Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
#   or whatever is there if the string is less than length 3. Return n copies of the front


def front_times(string, n):
    return string[0:3] * n if len(string) >= 3 else string * n


print(front_times('Chocolate', 2))  # → 'ChoCho'
print(front_times('Chocolate', 3))  # → 'ChoChoCho'
print(front_times('Abc', 3))  # → 'AbcAbcAbc'
