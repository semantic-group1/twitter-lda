import argparse
import json
import time
import sys
import boto
import bleach
from bs4 import BeautifulSoup
from boto.dynamodb2.table import Table
from boto.s3.key import Key 
from urllib2 import urlopen
import re
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

parser = argparse.ArgumentParser(description='Tweets Collection for TREC 2011')

parser.add_argument('date',action="store")
parser.add_argument('-s',action="store", default="0")
parser.add_argument('-e',action="store", default="99")

results = parser.parse_args()

tt = Table('tweets-soup')
s3 = boto.connect_s3()
b = s3.get_bucket('ik2342_tweets')
k = Key(b)
cf = 0
acf = 0
for fc in xrange(int(results.s),int(results.e)+1):
	# The Key is organised date as ids/20110223/20110223-000.dat ...
	k.key = "ids/"+str(results.date)+"/"+str(results.date)+"-"+str(fc).zfill(3)+".dat"
	print k.key
	cf = 0
	acf =0
	content = k.get_contents_as_string()
	content = content.split("\n")[:-1]
	content = [a.split() for a in content]
	data =dict()
	ot = dict()
	ptext = dict()
	for c in content:
		try:
			url = 'https://www.twitter.com/%s/status/%s' % (c[1],c[0])
			html = urlopen(url)
			#print url
			#print html.getcode()
			soup = BeautifulSoup(html)
			mypar = soup.find_all("p", { "class" : "js-tweet-text tweet-text" })
			p = mypar[1]
			html = p.contents
			clean = "".join([bleach.clean(a, tags=[], strip=True) for a in html])
			#print clean
			onlytext=[]
			hashtags =[]
			hyperlinks = []
			for word in clean.split():
				if not (word.startswith("@") or word.startswith("#") or word.startswith("http")):
					onlytext.append(word)
				elif word.startswith("#"):
					hashtags.append(word)
				elif word.startswith("http"):
					hyperlinks.append(word)
			j = dict()
			j['id']=int(c[0])
			j['user_id']=c[1]
			j['text']=clean
			j['file']=str(results.date)+"-"+str(fc).zfill(3)
			j['filedate']=str(results.date)
			j['filenumber']=str(fc).zfill(3)
			j['onlytext']=" ".join(onlytext)
			j['hashtags']="|".join(hashtags)
			j['hyperlinks']="|".join(hyperlinks)
			ot[int(c[0])]=j['onlytext']
			# First re code to separate out non-alphanumeric
			res = " ".join([stemmer.stem(re.sub(r'[\W_]',"",kw)) for kw in j['onlytext'].split(" ")])
			j['ptext']=res
			data[int(c[0])]=j
			ptext[int(c[0])]=res
			#print res
			#print j['onlytext']
			#print j
			#tt.put_item(data=j,overwrite=True)
			acf +=1
		except:
			pass
		cf+=1
		print str(cf)+"("+str(acf)+")",
		sys.stdout.flush()
	fn=str(results.date)+"-"+str(fc).zfill(3)+".json"
	with open("output/"+fn, 'w') as outfile:
  		json.dump(data, outfile)
	with open("output/t-"+fn, 'w') as outfile:
		json.dump(ot,outfile)
	with open("output/p-"+fn,'w') as outfile:
		json.dump(ptext,outfile)
	k.key = "output/"+str(results.date)+"/"+fn
	k.set_contents_from_filename("output/"+fn)
	k.key = "only/"+str(results.date)+"/"+fn
	k.set_contents_from_filename("output/t-"+fn)
	k.key = "ptext/"+str(results.date)+"/"+fn
	k.set_contents_from_filename("output/p-"+fn)
