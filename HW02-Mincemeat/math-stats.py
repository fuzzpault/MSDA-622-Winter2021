#!/usr/bin/env python
'''
Name: Paul Talaga
Date: March 22, 2021
Desc: Example solution to HW02 - Math statistics

'''

import mincemeat
import os, sys
import math


# Reads all the .nums files
data = []
incr = 0
# List all the nums files in this array
filenames = ['small.nums']

# Open all .nums files and read them line by line, as arrays of numbers
# Each row of numbers will be sent to a single mapper.
for filename in filenames:
    with open(filename) as file:
        line = file.readline()
        line_count = 0
        while line:
            data.append(map(float,line.split()))
            line = file.readline()
            line_count += 1
            incr += 1
        print("{} read.".format(filename))

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

#  print(datasource)

def mapfn(k, v):
    # Each v will be an array of numbers, one line from the nums file.
    yield "count", len(v)
    yield "sum", sum(v)
    yield "max", max(v)
    yield "min", min(v)
    for number in v:
        yield "sum2",number * number

def reducefn(k, vs):
    #print k,vs
    #Based on the key, 'reduce' something differnt.
    if k == 'max':
        return max(vs)
    elif k == 'min':
        return min(vs)
    else:
        return sum(vs)

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results

# This final Standard Deviation calcuation is allowable to be done after map/reduce as it does not get more
# mathematically complicated as the size (number of input numbers) increases.
# This is O(1) - the length of time for calculation does not depend on the size of the input - it is constant time
# See https://en.wikipedia.org/wiki/Big_O_notation
mean = results['sum'] / results['count']
print "Stdev:", math.sqrt(results['sum2'] / results['count'] - mean * mean)
