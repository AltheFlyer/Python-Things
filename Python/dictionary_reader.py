#DictionaryReader.py
#Allen Liu
#August 14, 2018
#########################DESCRIPTION#########################
#Reads text from one file and adds it to a word count
#It's a copy of something I started in java,
#but python may be slightly less dumb about this.
#A precusor to what may become a markov chain experiment
#Or a zipf analyzer.
#The file to read from is read.txt
#The file to write to is map.txt
#############################################################

import os.path

#Two dictionaries
#This is for what is newly read
count = {}
#This gets saved to a file
store = {}

readfile = open("read.txt", "r")
storage = open("map.txt", "r")

#Lines
lines = readfile.readlines()
readfile.close()

#Get values in readfile:
for line in lines:
    #Get words from each line
    words = line.split()
    #Word counter
    for word in words:
        word = word.replace(",", "")
        word = word.replace(".", "")
        word = word.replace(":", "")
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1

#Get stored values:
lines = storage.readlines()
storage.close()

for line in lines:
    #Get words from each line
    words = line.split()
    store[words[0]] = int(words[1])

#Print findings
##print("In text:")
##for key in count.keys():
##    print("{:10} : {}".format(key, count[key]))
##
##print("Already stored:")
##for key in store.keys():
##    print("{:10} : {}".format(key, store[key]))

#Update storage
for key in count.keys():
    if key in store:
        store[key] = store[key] + count[key]
    else:
        store[key] = count[key]

##print("Updated list:")
##for key in store.keys():
##    print("{:10} : {}".format(key, store[key]))

#Write to map file:
updater = open("map.txt", "w")

for key in store.keys():
    out = "{} {}\n".format(key, store[key])
    updater.write(out)

updater.close()
