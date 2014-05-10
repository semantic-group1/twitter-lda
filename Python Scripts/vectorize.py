#Author : Kanniah , Ilambharathi
#Description : This file changes queries to query vector from term by topic matrix

import glob
import gzip
import re
import string
import math
import sys
from math import log
from collections import defaultdict
if len(sys.argv)<2:
        print "Usage: python comp.py <input-folder-path> <queryfile>"
        exit()
results = sys.argv[1]
queryfile = sys.argv[2]

path = results+"/*"  
files=glob.glob(path)  

tt=dict(defaultdict(float))
td=dict(defaultdict(float))
for file in files: 
        data = open(file).readlines()
	#print data[0]
	data = [d.split("\t")[1][1:-2] for d in data]
	data = [d.split(",") for d in data]
	data = [[[f.split(":")[0],f.split(":")[1]] for f in d] for d in data]
	for i,d in enumerate(data):
		for f in d:
			if f[0] not in tt:
				tt[f[0]]=defaultdict(float)
			tt[f[0]][i]=float(f[1])
			if i not in td:
				td[i]=defaultdict(float)
			td[i][f[0]]=float(f[1])

queries= open(queryfile).readlines()
for query in queries:
	tq=[0.0]*400
	for q in query.split():
		#print q
		for i in xrange(0,400):
			if q in tt:
				tq[i]+=tt[q][i];

	for i in xrange(0,400):
		tq[i]=tq[i]/float(len(query.split()));
	print " ".join(map(str, tq))




