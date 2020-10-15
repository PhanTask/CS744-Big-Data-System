#!/bin/sh

time /mnt/data/hadoop/spark-2.4.7-bin-hadoop2.7/bin/spark-submit \
  --master spark://10.10.1.1:7077 \
  part3_function_memory.py "hdfs://10.10.1.1:9000/web-BerkStan.txt" "hdfs://10.10.1.1:9000/task3_output_memoryonly" 4 \
  1000
