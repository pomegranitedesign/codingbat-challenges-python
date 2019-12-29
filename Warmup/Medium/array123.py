# Dmitriy Shin
# December 29, 2019
# Difficulty: Medium

# Description
#   Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere


def array123(arr=[]):
    copy = arr
    output = []
    copy.sort()
    for i in range(len(copy)):
        if copy[i] not in output:
            output.append(copy[i])
    return output == [1, 2, 3]


print(array123([1, 1, 2, 3, 1]))  # → True
print(array123([1, 1, 2, 4, 1]))  # → False
print(array123([1, 1, 2, 1, 2, 3]))  # → True
