#!/bin/sh

../spark-2.4.7-bin-hadoop2.7/bin/spark-submit \
  --master spark://10.10.1.1:7077 \
  part2_py.py \
  1000
