# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyspark import SparkContext, SparkConf, StorageLevel  

# Set input and output path  
input_file = sys.argv[1]
output_file = sys.argv[2]
partition_num = int(sys.argv[3])

# Set spark configuration and spark context  
conf = SparkConf().setAppName("part3").setMaster("local")  
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")  

# Read the input file as RDD
#  Here we followed the RDD paper implementation closely
# we first filter the data with "#", then split each row to get keys and values. 
# Then we did the persistence (cache setting) for the data.
lines = sc.textFile(input_file).filter(lambda line:'#' not in line).map(lambda line:line.split("\t",1)).persist(storageLevel=StorageLevel(False,True,False,False,1))

# group by key operation
node_map = lines.groupByKey()

# generate initial rank
rank = node_map.mapValues(lambda e: 1.0)

# Run ten iterations with each recalculating a rank for every node based on PageRank # algorithm
#   Contribution is calculated following https://en.wikipedia.org/wiki/PageRank and original RDD paper
for i in range(10):
    contribution = node_map.join(rank).flatMap(lambda rn: [(to_id, rn[1][1] / rn[1][0].__len__()) for to_id in rn[1][0]]).reduceByKey(lambda rn1, rn2: rn1 + rn2)
    rank = contribution.mapValues(lambda cr: 0.15 + 0.85 * cr)
    break


# reformat the output. not really needed
# res = rank.map(lambda r: ','.join(str(w) for w in r))  

# save result
rank.repartition(1).saveAsTextFile(output_file) 
