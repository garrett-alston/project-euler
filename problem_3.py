#!/usr/bin/env python3
import numpy as np


def problem_N():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    
    What is the largest prime factor of the number 600851475143 ?
    """
    N=600851475143
    sqrtN = np.sqrt(N)
    n=2
    largestDivisor=0
    while n <= N:
        if N % n == 0:
            N = N // n
            largestDivisor=n
            print("Largest divisor so far:",largestDivisor)
        else:
            n+=1
    return largestDivisor



if __name__ == "__main__":
    print( "Answer:", problem_N() )
