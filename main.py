# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:15:46 2019

@author: onec
"""

import matplotlib.pyplot as plot
import matplotlib.cm as cm
import numpy as np
import random
import re
from mathfunctions import np_sieve

if __name__=='__main__':
    print("Initializing Prime Sequence")

    #
    # Initialize Sequence of Primes in Range
    #
    ceiling = 2**20 # Ceiling of Prime Sequence
    primes = np_sieve(ceiling)
    numberOfPrimes = primes.__len__()
    minprime = primes[0]
    maxprime = primes[numberOfPrimes - 1]
    print ("Generated list of %s primes" % numberOfPrimes)

    length_of_recurrence = 100
    recurrence_sequence = np.zeros(length_of_recurrence)
    recurrence_sequence[0] = 0
    recurrence_sequence[1] = 1
    
    rolling_index = 0
    
    fibonacci_prime_sequence = []
    fibonacci_prime_sequence_mod29 = []
    fibonacci_mod29_prime_sequence = []

    for x in range(2, length_of_recurrence):
        recurrence_sequence[x] = recurrence_sequence[x - 1] + recurrence_sequence[x - 2]
        rolling_index += recurrence_sequence[x] % 29      
        #print ('%s' % rolling_index)
        if recurrence_sequence[x] < numberOfPrimes:
            index = primes[int(recurrence_sequence[x])]
            print ('%s' % index)
            fibonacci_prime_sequence.append(index)
            print ('%s' % int(index%29))
            fibonacci_prime_sequence_mod29.append(int(index%29))
            print ('%s' % rolling_index)
            fibonacci_mod29_prime_sequence.append(int(rolling_index))
            
    print(fibonacci_prime_sequence)
    print(fibonacci_prime_sequence_mod29)
    print(fibonacci_mod29_prime_sequence)



    #input("Press [Enter] to continue.")


