#!/usr/bin/env python
'''
Name: Paul Talaga
Date: March 22, 2021
Desc: Example solution to HW02 - Finding primes which are palindromes.

'''
import mincemeat

# To minimize network overhead, each map job is given a single number, which specifies a range of value
# to check for prime-ness and palindrome-ness. 
# Each job will check 10000 values
#data = range(1000)
data = range(10)  # This will check from 0 to 10*10000 or 0 to 100,000
# The data source can be any dictionary-like object
datasource = dict(enumerate(data))
#print datasource

def mapfn(k, value):
    #print "Map",k,v
    for v in range(value*10000, (value+1)*10000 ):
        #print "Map",k,v
        correct = True
        for i in range(2,v):
            if (v % i) == 0:
                correct = False
    
        if str(v) !=  str(v)[::-1]:
            correct = False
        if correct:
            yield 'found one!', v
    #if str(v) ==  str(v)[::-1]:
    #   yield 'found one!', k
        #print "not palindrome", v
        #return
    

def reducefn(k, vs):
    # Nothing to do!  Just pass through!
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
