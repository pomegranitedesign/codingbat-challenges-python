# Dmitriy Shin
# December 29, 2019
# Difficulty: Medium

# Description
#   Given a non-empty string like "Code" return a string like "CCoCodCode".


def string_splosion(string):
    output = []
    while len(string) > 0:
        output.append(string)
        string = string[:-1:1]
    output.reverse()
    return "".join(output)


print(string_splosion('Code'))  # → 'CCoCodCode'
print(string_splosion('abc'))  # → 'aababc'
print(string_splosion('ab'))  # → 'aab'
