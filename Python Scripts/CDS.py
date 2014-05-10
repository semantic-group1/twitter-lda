#Author: Patel,Umang
#Objective: This file calculated the CDS and displays top 10 results

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


from sys import argv

filename1= sys.argv[1]
filename2= sys.argv[2]
txt2 = open(filename2)

for l2 in txt2:

	templist=[]
	vector1=l2.split(" ")
	vector1[-1]=vector1[-1].strip("\n")

	txt1 = open(filename1,"r")
	for l1 in txt1:
	
		temp=l1.split(" ")
		temp[-1]=temp[-1].strip("\n")
		f1=map(float,temp)
		f2=map(float,vector1)
		sum1=sum([i*j for i, j in zip(f1,f2)])
		deno=math.sqrt(sum([ii**2 for ii in f1]))*math.sqrt(sum([i**2 for i in f2]))
		if deno !=0:
			templist.append(sum1/deno)
	#print templist
	dummy=sorted(range(len(templist)), key=lambda i: templist[i], reverse=True)[:10] #change  5 here to change top n elements 
	dummynewlist = [x+1 for x in dummy]
	dummynewlist =[ str(x)+"_"+filename1 for x in dummynewlist]
	dummy2=sorted(templist, reverse=True)[:10]
	print dict(zip(dummynewlist,dummy2))


