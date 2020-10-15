#!/bin/sh

for i in 1 4 16 256 512 1024
do
(time /mnt/data/hadoop/spark-2.4.7-bin-hadoop2.7/bin/spark-submit \
  --master spark://10.10.1.1:7077 \
  part3_pagerank.py "hdfs://10.10.1.1:9000/web-BerkStan.txt" "hdfs://10.10.1.1:9000/task2_output"${i} ${i} \
  1000) > "function_memory"${i}  2>&1

(time /mnt/data/hadoop/spark-2.4.7-bin-hadoop2.7/bin/spark-submit \
  --master spark://10.10.1.1:7077 \
  part3_pagerank_large.py "hdfs://10.10.1.1:9000/enwiki-pages-articles" "hdfs://10.10.1.1:9000/task2_output_large"${i} ${i} \
  1000) > "function_memory_large"${i}  2>&1
done
