#!/bin/sh
#Author:Dash,Sarthak
#Removes stop words.

stopFile=$1

stopLines=`cat $stopFile | wc -l`
stopcount=1


  while [ $stopcount -le $stopLines ]
  do
	wrd=`head -n $stopcount $stopFile | tail -1`
	sed -e "s/"$wrd"//g" -i *
	echo "Word $wrd removed"
	(( stopcount++ ))
  done

  
	
