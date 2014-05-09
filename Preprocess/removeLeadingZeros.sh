#!/bin/sh
#Author:Dash,Sarthak
#Objective:Removes Leading zeros from the filenames, so that it can be easily processed by Columbia's YETI cluster

ls quarter > temp.txt
lines=`cat temp.txt | wc -l`
count=1
while [ $count -le $lines ]
do
  file=`head -n $count temp.txt | tail -1`
  partA=`echo $file | cut -d"-" -f1`	
  partB=`echo $file | cut -d"-" -f2`
  partC=`echo $partB | sed 's/^0*//g'`
  newfile=$partA"-"$partC
  mv "quarter/"$file "quarter/"$newfile
  (( count++ ))
done

