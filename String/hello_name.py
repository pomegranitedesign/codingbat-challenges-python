# Dmitriy Shin
# December 29, 2019
# hello_name.py
# Description
#   Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


def hello_name(name):
    return "Hello " + name + "!"


print(hello_name('Bob'))  # → 'Hello Bob!'
print(hello_name('Alice'))  # → 'Hello Alice!'
print(hello_name('X'))  # → 'Hello X!'
