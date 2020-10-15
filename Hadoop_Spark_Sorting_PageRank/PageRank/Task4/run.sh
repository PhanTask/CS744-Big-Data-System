#!/bin/sh

(time /mnt/data/hadoop/spark-2.4.7-bin-hadoop2.7/bin/spark-submit \
  --master spark://10.10.1.1:7077 \
  part3_pagerank.py "hdfs://10.10.1.1:9000/enwiki-pages-articles" "hdfs://10.10.1.1:9000/task4_output" 16 \
  1000) > "task4_output_log" 2>&1

