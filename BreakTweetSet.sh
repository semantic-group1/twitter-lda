#!/bin/sh
#Author: Dash,Sarthak
#Objective: Break each tweet into a separate file.

FOLDER="InputDocuments/"
FILE="TweetsInputData"

# Clean up the folder if required.
rm $FOLDER"*"

lines=`cat $FILE | wc -l`
count=1
while [ $count -le $lines ]
do
  newFile=$FOLDER"File-"$count
  touch $newFile
  line=`head -n $count $FILE | tail -1`
  echo $line >> $newFile
  (( count++ ))
done
