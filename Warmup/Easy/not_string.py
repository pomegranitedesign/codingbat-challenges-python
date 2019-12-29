# Dmitriy Shin
# December 29, 2019
# Difficulty: Easy

# Description
# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.


def not_string(string=""):
    return "not " + string if ("not " not in string or "not" not in string) and string != "not" else string


print(not_string('candy'))  # → 'not candy'
print(not_string('x'))  # → 'not x'
print(not_string('not bad'))  # → 'not bad'
