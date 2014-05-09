#Author: Patel,Umang
#Objective: This file takes two folders as input (agr1- folders containing CDS results , arg2-folders containing tweets) and displays top tweets of CDS results.



import glob
import gzip
import re
import string
import math
import sys
from math import log
from collections import defaultdict
if len(sys.argv)<2:
        print "Usage: python comp.py <input-path>"
        exit()


results = sys.argv[1]
results2 = sys.argv[2]


path = results+"/*"  
files=glob.glob(path)  


path2 = results2+"/*"  
files2=glob.glob(path2)

 

tt=dict(defaultdict(float))
td=dict(defaultdict(float))

all1=list() 

filenames=[]

for file in files: 

        data = open(file).readlines()
        all1.append(data)
        

counter=0

for i in xrange(0,len(all1[0])):  

	#print i
	temp=[]
	for j in xrange(0,len(all1)):

		
		temp2=all1[j][i]
		#print temp2
		temp2=temp2.replace('{','')
		temp2=temp2.replace('}','')
		temp2=temp2.strip("\n")

		if temp2.split(",")!=['']:
			temp.extend(temp2.split(","))

	

	key1=[]
	value1=[]	
	
	for k in temp:

		
		
		t2=k.split(":")[0]
		key1.append(t2.strip(" "))
		t3=k.split(":")[1]
		value1.append(t3.strip(" "))


	zipped = zip(value1, key1)
	zipped.sort(reverse=True)	
	value1 = [i for (i, s) in zipped]
	key1 = [s for (i, s) in zipped]
	
	keytemp=[]
	line=[]

	for i in key1:
		line.append((i.split("_")[0]).split("'")[1])
		keytemp.append((i.split("/")[-1]).replace(".outputmat'",""))


	for kk in xrange(0,len(keytemp)):
		data = open(results2+keytemp[kk]).readlines()
		print data[int(line[kk])]
		counter=counter+1
		
	print "__________________________________________________________________________________"
	