"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    strItems = []
    # Your code goes here
    for x in items:
        strItems.append(str(x))

    for i in strItems:

        if (i in frequencies):
         frequencies[i] += 1
        else:
         frequencies[i] = 1

    return frequencies
