#!/bin/sh
#Author: Dash, Sarthak

queryFile=$1

if [ $queryFile == "compile" ]
then
	# Compiling the java file.
	javac -cp build/core/lucene-core-4.8-SNAPSHOT.jar:build/demo/lucene-demo-4.8-SNAPSHOT.jar:build/analysis/common/lucene-analyzers-common-4.8-SNAPSHOT.jar:build/queryparser/lucene-queryparser-4.8-SNAPSHOT.jar demo/src/java/org/apache/lucene/demo/SearchFiles.java

else

	# Running the search query operation.
	java -cp build/core/lucene-core-4.8-SNAPSHOT.jar:build/demo/lucene-demo-4.8-SNAPSHOT.jar:build/analysis/common/lucene-analyzers-common-4.8-SNAPSHOT.jar:build/queryparser/lucene-queryparser-4.8-SNAPSHOT.jar org.apache.lucene.demo.SearchFiles -index IndexDir -queries $queryFile -paging 1000

fi
