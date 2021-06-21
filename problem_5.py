#!/usr/bin/env python3
import numpy as np


def problem_5():
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    """
    highestDivisor=1
    n=2520
    while highestDivisor<20:
        highestCurrentDivisor=1
        for i in range(1,21):
            if n%i==0:
                highestCurrentDivisor=i
            else:
                break
        if highestCurrentDivisor>highestDivisor:
            highestDivisor=highestCurrentDivisor
            print("Highest divisor:",highestDivisor)
        n=n+1
    return n-1



if __name__ == "__main__":
    print( "Answer:", problem_5() )
