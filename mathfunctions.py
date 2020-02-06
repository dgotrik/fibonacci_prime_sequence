# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:23:07 2019

@author: onec
"""
import numpy as np


#From https://sanghan.xyz/blog/2014/09/sieve/
def np_sieve(n: int) -> np.ndarray:
    """
    Sieve with it's guts swapped with numpy
    ndarray
    """
    primes = np.ones(n+1, dtype=np.bool)
    for i in np.arange(2, n**0.5+1, dtype=np.uint32):
        if primes[i]:
            primes[i*i::i] = False
    return np.nonzero(primes)[0][2:]

#From https://www.geeksforgeeks.org/sieve-of-eratosthenes/
def SieveOfEratosthenes(n): 
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            print(p)
            

