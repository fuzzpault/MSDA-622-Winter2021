#!/usr/bin/env python
import mincemeat
import os, sys


# Reads all the .nums files
data = []
incr = 0
filename = 'small.nums'	 # Change this to be whatever nums file you want.

with open(filename) as file:
    line = file.readline()
    line_count = 0
    while line:
        data.append(map(float,line.split()))
        line = file.readline()
        line_count += 1
        incr += 1
    print(filename, " read.")

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

#  print(datasource)

def mapfn(k, v):
    yield "change","me"

def reducefn(k, vs):
    result = len(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
