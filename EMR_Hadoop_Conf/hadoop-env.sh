#!/bin/bash

export HADOOP_HEAPSIZE="19000"
export HADOOP_DATANODE_HEAPSIZE="1064"
export HADOOP_NAMENODE_HEAPSIZE="3276"
export HADOOP_JOBTRACKER_HEAPSIZE="6758"
export HADOOP_TASKTRACKER_HEAPSIZE="839"
export HADOOP_OPTS="$HADOOP_OPTS -server"
if [ -e /home/hadoop/conf/hadoop-user-env.sh ] ; then
  . /home/hadoop/conf/hadoop-user-env.sh
fi
