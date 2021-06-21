#!/usr/bin/env python3
import numpy as np
import itertools

def isPalindrome(n):
    nAsString=str(n)
    return nAsString[::-1]==nAsString


def problem_4():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    highestPalindromeSofar=0
    for i,j in itertools.product(range(100,1000),range(100,1000)):
        n=i*j
        if(isPalindrome(n) and n>highestPalindromeSofar):
            highestPalindromeSofar=n
            print("Highest palindrome so far:",highestPalindromeSofar)
    return highestPalindromeSofar



if __name__ == "__main__":
    print( "Answer:", problem_4() )
