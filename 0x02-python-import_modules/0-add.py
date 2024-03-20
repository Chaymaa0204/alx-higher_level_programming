#!/usr/bin/python3
a = 1
b = 2
add_0 = __import__("add_0").add
print("{} + {} = {}".format(a, b, add_0(a, b)))

# Importing the 0-add.py script
__import__("0-add")

