# !/bin/sh
# Author: Dash,Sarthak
# Objective: Index documents so as to be used by Lucene.

compile=$1
InputDocuments=$2

if [ -d IndexDir ]
then
  rm -rf IndexDir
fi

mkdir IndexDir

if [ $compile == "compile" ]
then
	#compiling the java file
	javac -cp build/core/lucene-core-4.8-SNAPSHOT.jar:build/demo/lucene-demo-4.8-SNAPSHOT.jar:build/analysis/common/lucene-analyzers-common-4.8-SNAPSHOT.jar:build/queryparser/lucene-queryparser-4.8-SNAPSHOT.jar demo/src/java/org/apache/lucene/demo/IndexFiles.java

else

	#indexing the documents.
	java -cp build/core/lucene-core-4.8-SNAPSHOT.jar:build/demo/lucene-demo-4.8-SNAPSHOT.jar:build/analysis/common/lucene-analyzers-common-4.8-SNAPSHOT.jar:build/queryparser/lucene-queryparser-4.8-SNAPSHOT.jar org.apache.lucene.demo.IndexFiles -docs $InputDocuments -update true -index IndexDir

fi
