import sys 
from pyspark import SparkContext, SparkConf, StorageLevel 
  
# Set input and output path 
input_file = sys.argv[1] 
output_file = sys.argv[2] 
partition_num = int(sys.argv[3]) 

# Set spark configuration and spark context 
conf = SparkConf().setAppName("part3").setMaster("local") 
sc = SparkContext(conf=conf) 

# Read the input file as RDD 
lines = sc.textFile(input_file) 

# Parse the RDD file to be pairs of nodes (i.e., (from_id, to_id)) 
lines = lines.filter(lambda line:'#' not in line) 
node_pairs = lines.map(lambda line:line.split("\t")) 
 
# Drop the node pair RDD to either disk or memory as the storage level specifies  
node_pairs = node_pairs.persist(storageLevel=StorageLevel(False,True,False,False,1)) 

# Reorganize the node pairs into a node map 
node_map = node_pairs.groupByKey() 
 
# Set the initial rank of each node as 1  
rank = node_map.mapValues(lambda e: 1.0) 

# Run ten iterations with each recalculating a rank for every node based on PageRank # algorithm   
for i in range(10): 
    rank_node_map = rank.join(node_map).partitionBy(partition_num) 
    contribution_mapped = rank_node_map.flatMap(lambda rn: [(to_id, rn[1][0] / rn[1][1].__len__()) for to_id in rn[1][1]]) 
    contribution_reduced = contribution_mapped.reduceByKey(lambda rn1, rn2: rn1 + rn2) 
    rank = contribution_reduced.mapValues(lambda cr: 0.15 + 0.85 * cr) 

# Save the final rank RDD to an output file 
rank.repartition(1).saveAsTextFile(output_file) 
