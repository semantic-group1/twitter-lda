Twitter Semantic Search Project 
===========

Twitter Semantic Project using Latent Dirichlet Allocation (LDA)

Setting up the Environment
====
You could either use virtualenv and run the following command after activating the virtualenv or just run it in the terminal. Update the .boto file with Valid AWS Credential Keys.
    
    pip install -r Tweets_Collect/requirements.txt
    
Code Help on Tweets Collection
====
    python Tweets_Collect/tweets_collect.py -h
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

    python Tweets_Collect/tweets_collect.py 20110128 -s 20 -e 88
  
The above code will collect tweets for the TweetsID in for the date 2011-01-28 from files 20 to 88 (inclusive) and write 2 files for each file. One containing all the data and the other containing only the cleaned (processed - removed hashtags, hyperlinks, stemmed (using Porter Stemmer))

Generating Sequence Files for Tweets
====

    hadoop jar SequenceFileWrite.jar com.sarcasm.dpp.SequenceFileWriteDemo <InputFileNameContainingAllTweets> <OutputSeqFileName>
   
 The above code accepts a file containing all the tweets and prepares a sequence file wherein the key of the sequence file equals the TweetID and the value equals the Tweet. This forms the input for the second stage of Mahout cvb program.  

Apache Lucene Scripts
====
To use Lucene Indexer to index all the files in the given directory,

    ./indexDocuments.sh <command> <InputDirectory>
    
To search for queries (in a queryfile) across the Lucene index, we use the following script

    ./searchDocuments.sh <command/queryFile>

Apache Mahout (Collapsed Variational Bayes Algorithm - CVB)
===
    
    hadoop jar mahout-examples-0.8-job.jar org.apache.mahout.text.SequenceFilesFromDirectory -i /se/dataset -o /se/outputseq -xm sequential
    ./mahout seq2sparse -i /se/outputseq -o /se/outputsparsedvec --namedVector -wt tf
    ./mahout rowid -i /mahoutlda/outputsparsedvec/tf-vectors -o /mahoutlda/matrix
    ./mahout cvb -i /mahoutlda/matrix/matrix -o /mahoutlda/lda-output -mt /mahoutlda/ldaoutput/models -dt /mahoutlda/ldaoutput/docTopics -dict /mahoutlda/outputsparsedvec/dictionary.file-0 -k 400 -x 40 -ow
    ./mahout vectordump -i /mahoutlda/ldaoutput/docTopics -o /mahoutlda/ldaoutput/output-docTopics -p true -d /mahoutlda/outputsparsedvec/dictionary.file-0 -dt sequencefile -sort /mahoutlda/ldaoutput/docTopics 
    ./mahout vectordump -i /mahoutlda/ldaoutput/model/model-1 -o /mahoutlda/ldaoutput/output-model-1 -p true -d /mahoutlda/outputsparsedvec/dictionary.file-0 -dt sequencefile -sort /mahoutlda/ldaoutput/models/model-1
