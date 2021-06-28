#!/usr/bin/env python3
import numpy as np


def isPrimeData(N):
    data = np.ndarray(N,dtype=bool)
    data[...]=True
    data[0]=False # don't count 1 as a prime
    stop=int(np.sqrt(N))+1
    for i in range(1,stop):
        if data[i]==False:
            continue
        data[2*i+1::i+1]=False
    return data


def problem_7():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    
    What is the 10 001st prime number?
    """
    N=1000000
    isPrimeArray=isPrimeData(N)
    primes=[i+1 for i,x in enumerate(isPrimeArray) if x]
    print(len(primes))
    return primes[10000]



if __name__ == "__main__":
    print( "Answer:", problem_7() )
