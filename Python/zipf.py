#Zipf.py
#Allen Liu
#August 15, 2018
#########################DESCRIPTION#########################
#Lets try zipf stats
#This was a mistake
#############################################################

import os.path
import operator
from fractions import gcd

readfile = open("map.txt", "r")

collection = {}

lines = readfile.readlines()

for line in lines:
    words = line.split()
    collection[words[0]] = int(words[1])

#Converts dict to a sorted list of tuples
sorted_set = sorted(collection.items(), key=operator.itemgetter(1))

most_common = sorted_set[len(sorted_set) - 1][0]
maximum = sorted_set[len(sorted_set) - 1][1]

for key in sorted_set:
    gcf = gcd(key[1], maximum)
    print("{:20} : {:0}/{:0} ({})".format(key[0], key[1] / gcf, maximum / gcf, key[1] / maximum))
