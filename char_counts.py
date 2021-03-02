#!/usr/bin/env python
import mincemeat

data = ["Humpty Dumpty sat on a wall",
        "Humpty Dumpty had a great fall",
        "All the King's horses and all the King's men",
        "Couldn't put Humpty together again",
        ]
# The data source can be any dictionary-like object
datasource = dict(enumerate(data))
#print datasource

def mapfn(k, v):
    #print "Map",k,v
    counter = 0
    for c in v:
    	#print "map", c, 1
    	yield c, 1
    	counter += 1
    yield 'total', counter

def reducefn(k, vs):
    print "Reduce", k, vs
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results

for key in results:
	if key != 'total':
		print key, results[key] / float(results['total'])
