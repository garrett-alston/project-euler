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

def primes(N):
    """
    Returns array of all primes p <= N.
    """
    isPrimeArray=isPrimeData(N)
    primes=[i+1 for i,x in enumerate(isPrimeArray) if x]
    return primes

if __name__ == "__main__":
    print( "Primes <=23:", primes(23) )
