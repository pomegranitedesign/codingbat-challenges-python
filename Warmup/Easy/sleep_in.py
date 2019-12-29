# Dmitriy Shin
# December 29, 2019
# Difficulty: Easy

# Description
#  The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
#  We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


# Since we know the rules, its all about the logic
# we are sleeping in if its not a weekday or we are on vacation, its that simple
def sleep_in(weekday, vacation):
    return not weekday or vacation


print(sleep_in(False, False))  # → True
print(sleep_in(True, False))  # → False
print(sleep_in(False, True))  # → True
