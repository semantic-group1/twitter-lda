Twitter Semantic Search Project 
===========

Twitter Semantic Project using Latent Dirichlet Allocation (LDA)

Setting up the Environment
====
You could either use virtualenv and run the following command after activating the virtualenv or just run it in the terminal. Update the .boto file with Valid AWS Credential Keys.
    
    pip install -r Tweets_Collect/requirements.txt
    
Code Help on Tweets Collection
====
    python Tweets/Collect/tweets_collect.py -h
    usage: tt3.py [-h] [-s S] [-e E] date
    Tweets Collection for TREC 2011
    positional arguments:
        date
    optional arguments:
        -h, --help  show this help message and exit
        -s Start file number
        -e End file number

Run the Twitter Collection Code
====

    python Tweets_Collection/tweets_collect.py 20110128 -s 20 -e 88
  
The above code will collect tweets for the TweetsID in for the date 2011-01-28 from files 20 to 88 (inclusive) and write 2 files for each file. One containing all the data and the other containing only the cleaned (processed - removed hashtags, hyperlinks, stemmed (using Porter Stemmer))

Generating Sequence Files for Tweets
====

    hadoop jar SequenceFileWrite.jar com.sarcasm.dpp.SequenceFileWriteDemo <InputFileNameContainingAllTweets> <OutputSeqFileName>
   
 The above code accepts a file containing all the tweets and prepares a sequence file wherein the key of the sequence file equals the TweetID and the value equals the Tweet. This forms the input for the second stage of Mahout cvb program.  
