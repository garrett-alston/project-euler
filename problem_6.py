#!/usr/bin/env python3
import numpy as np

def difference(n):
    d=0
    for i,j in np.ndindex(n,n):
        i=i+1
        j=j+1
        if i>=j:
            continue
        d+=2*i*j
    return d

def problem_6():
    """
    The sum of the squares of the first ten natural numbers is,

    The square of the sum of the first ten natural numbers is,

    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

    .

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    return difference(100)



if __name__ == "__main__":
    print( "Answer:", problem_6() )
