# Dmitriy Shin
# December 29, 2019
# make_abba.py
# Description
#   Given two strings, a and b, return the result of putting them together
#   in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".


def make_abba(a, b):
    return (a + b) + (b + a)


print(make_abba('Hi', 'Bye'))  # → 'HiByeByeHi'
print(make_abba('Yo', 'Alice'))  # → 'YoAliceAliceYo'
print(make_abba('What', 'Up'))  # → 'WhatUpUpWhat'
