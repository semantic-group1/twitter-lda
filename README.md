Twitter Semantic Search Project 
===========

Twitter Semantic Project using Latent Dirichlet Allocation (LDA)


Run the Twitter Collection Code
====
  python tweets_collect.py 20110128 -s 20 -e 88
  
The above code will collect tweets for the TweetsID in for the date 2011-01-28 from files 20 to 88 (inclusive) and write 2 files for each file. One containing all the data and the other containing only the cleaned (processed - removed hashtags, hyperlinks, stemmed (using Porter Stemmer))
