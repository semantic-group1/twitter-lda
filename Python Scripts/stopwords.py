#Author: Patel,Umang
#Objective: This file removes the stopwords

import os
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

results=sys.argv[1]
filename2= sys.argv[2]

path = results+"/*"  
files=glob.glob(path)




data = open(filename2).readlines()
data=[ x.strip("\n") for x in data]

#print data

results=results.split("/")[1:-1]
results1="/".join(results)

results1="/"+results1
#print results1


if not os.path.exists(results1+"/output1"):
    os.makedirs("output1")

for file in files:

	
	ft=file.split(".")[0]
	ftname=ft.split("/")[-1]
	
	#print file
	txt1 = open(file)

	tempfile= open(results1+"/output1/"+ftname+"-O.txt",'w')

	for l1 in txt1:
		#print l1
		temp=l1.strip("\n")
		temp=temp.split(" ")

		for w1 in temp:
			if (w1 not in data):
				tempfile.write(w1+" ")
		tempfile.write("\n")	

	tempfile.close()