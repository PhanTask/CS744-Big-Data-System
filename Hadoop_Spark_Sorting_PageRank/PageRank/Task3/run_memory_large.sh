#!/bin/sh

time /mnt/data/hadoop/spark-2.4.7-bin-hadoop2.7/bin/spark-submit \
  --master spark://10.10.1.1:7077 \
  part3_function_memory_large.py "hdfs://10.10.1.1:9000/enwiki-pages-articles" "hdfs://10.10.1.1:9000/task3_output_large" 16 \
  1000
