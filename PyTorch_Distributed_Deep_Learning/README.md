There are two folders in total. 

**master** folder contains all codes run on the node 0. 

**other** folder contains all codes run on the node 1, node 2, node 3.

part1.py refers to the code for VGG11 model running on a single machine.

part2a.py refers to the code for VGG11 model running on multiple machines using **gather** and **scatter** functions.

In addtion to the part2a in the course material, we provide another approach in part2a_extra.py provides the code for VGG11 model running on multiple machines using **isend** and **irecv** functions.

part3.py refers to the code for VGG11 model running on multiple machines using **DDP** framework.

All codes can be executed with the following command:

```
python main.py --master-ip $ip_address$ --num-nodes 4 --rank $rank$
```