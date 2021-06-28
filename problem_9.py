#!/usr/bin/env python3
import numpy as np


def problem_9():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    N=1000
    for c in range(1,N):
        print(c)
        for b in range(1,c):
            a=1000-b-c
            if a**2+b**2==c**2:
                return a*b*c
    return 0



if __name__ == "__main__":
    print( "Answer:", problem_9() )
