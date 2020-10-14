from pyspark import SparkContext, SparkConf 

# set input and output path 
# input = "hdfs://10.10.1.1:9000/export.csv" 
input = "/mnt/data/hadoop/part2/export.csv" 
# output = "hdfs://10.10.1.1:9000/part2_output" 
output = "/mnt/data/hadoop/part2/part2_output" 

# Set spark configuration and spark context 
conf = SparkConf().setAppName("part2").setMaster("local") 
sc = SparkContext(conf=conf) 

# read the input and store it into RDD 
lines = sc.textFile(input) 

# check the first row 
print(lines.first()) 

# split each line by comma 
sep_lines = lines.map(lambda l: l.split(",")) 

# sort the data firstly by the country code alphabetically (the third column) 
# then by the timestamp (the last column) 
sorted_lines = sep_lines.sortBy(lambda l: l[2], lambda l : l[-1]) 

# generate and save outpput.csv file 
res = sorted_lines.map(lambda l: ','.join(str(w) for w in l)) 
res.repartition(1).saveAsTextFile(output) 
