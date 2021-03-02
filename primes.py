#!/usr/bin/env python
import mincemeat

data = range(300)
# The data source can be any dictionary-like object
datasource = dict(enumerate(data))
#print datasource

def mapfn(k, v):
    #print "Map",k,v
    for i in range(2,v):
    	if (v % i) == 0:
    		return
    yield 'found one!', k

def reducefn(k, vs):
    print "Reduce", k, vs
    #result = sum(vs)
    return vs

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
