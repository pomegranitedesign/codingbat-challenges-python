# Dmitriy Shin
# December 29, 2019
# first_half.py
# Description
#   Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


def first_half(string=""):
    return string[0:int(len(string) / 2)]


print(first_half('WooHoo'))  # → 'Woo'
print(first_half('HelloThere'))  # → 'Hello'
print(first_half('abcdef'))  # → 'abc'
