#!/usr/local/bin/python3

# Example Python program to find the primes from 1 to 100

import math

import sys
if sys.version_info[0] < 3:
	raise Exception("Must be using python 3")

primes = []   
for i in range(3, 100, 2):
    is_factor_found = False 
    for test in range(3, 1 + int(math.sqrt(i)//1), 2):
        #print (i, test, i%test)
        if i % test == 0:
            is_factor_found = True
            break
    if not is_factor_found:
        print (i)
        primes += [i]  # convert to list then append
        
print(primes)

