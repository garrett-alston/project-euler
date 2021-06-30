#!/usr/bin/env python3
import numpy as np
import prime

def problem_10():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    primesBelowTwoMillion = prime.primes(2000000)
    return sum(primesBelowTwoMillion)



if __name__ == "__main__":
    print( "Answer:", problem_10() )
