#!/usr/bin/env python
'''
Name: Paul Talaga
Date: March 22, 2021
Desc: Example solution to HW02 - Finding primes which are palindromes.

'''
import mincemeat
import os, sys


# Reads all the .nums files
data = []
incr = 0
filename = 'TimeMachine.txt'	 # Change this to be whatever nums file you want.

#search_term = 'confirmed'
search_term = raw_input("What should I search for?")

# To have each mapper search for a word that isn't hardcoded, embed the search term
# in the map data, so each mapper is getting a list [search term, line of text]

with open(filename) as file:
    line = file.readline()
    line_count = 0
    while line:
        data.append(  [search_term, line ] )
        line = file.readline()
        line_count += 1
        incr += 1
    print(filename, " read.")

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

#print(datasource)

def mapfn(k, v):
    (term, line) = v
    print v
    if term in line:
        yield "result",v

def reducefn(k, vs):
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
