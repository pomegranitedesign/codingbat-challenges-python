# Dmitriy Shin
# December 29, 2019
# Difficulty: Easy

# Description
#   Given a string, return a new string where the first and last chars have been exchanged.


def front_back(string):
    output = string

    if len(string) > 1 and string != " ":
        first_char = string[0]
        last_char = string[-1]
        output = last_char + string[1:-1] + first_char

    return output


print(front_back('code'))  # → 'eodc'
print(front_back('a'))  # → 'a'
print(front_back('ab'))  # → 'ba'
print(front_back('aavJ'))  # → 'Java'
