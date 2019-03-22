#!/usr/bin/python
# Filename: codenames.py
"""

"""

import random
from adjectives import adjectives as adjective
from nouns import nouns as noun

def codename(n=10):
    for i in range(n):
        word1 = random.choice(adjective)
        word2 = random.choice(noun)
        print(f"{word1} {word2}")
    return


if __name__ == "__main__":
    codename(20)