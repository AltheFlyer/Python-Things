#MarkovTexter.py
#Allen Liu
#August 14, 2018
#########################DESCRIPTION#########################
#Uses the mess of a databse to randomly generate text.
#############################################################

import os.path
import random

#Generate the damned matrix
reader = open("markov.txt", "r")

#Used to show start of a text
start_word_code = "qwertyuiopasdfghjklzxcvbnm"
#Used to show the end of a text
end_word_code = "mnbvcxzlkjhgfdsapoiuytrewq"
words = []
matrix = []
maximums = []

#Word list
lines = reader.readlines()
reader.close()
print("read")

for word in lines[0].split():
    if not (word in words):
        words.append(word)
print("worded")

del lines[0]
#Matrix generation
for line in lines:
    tmp_dict = {}
    values = line.split()
    for i in range(len(words)):
        tmp_dict[words[i]] = int(values[i])
    matrix.append(tmp_dict)
print("matrixed")

#Maximums for each index:
for m in matrix:
    sigma = 0
    for key in m.keys():
        sigma += m[key]
    maximums.append(sigma - 1)
print("maximized")

#Converts matrix to something suitible for rng
#Each value (sigma) represents what the rng value must be
#below for the index to be chosen
for i in range(len(matrix)):
    sigma = 0
    for key in matrix[i]:
        if matrix[i][key] != 0:
            sigma += matrix[i][key]
            matrix[i][key] = sigma
        else:
            matrix[i][key] = -1

print("converted")


#Output
cont = ""
early = False
while not cont == "stop":
    index = random.randint(0, len(words) - 3)
    count = 0

    out = ""
    while (not index == len(words) - 1):
        #The markoving
        r = random.randint(0, maximums[index])
        #A sorta dodgy way of getting the random chances to work
        for chance in matrix[index].keys():
            #Code above will order the values, so
            #the break helps prevent indices from automatically
            #becoming the highest value possible
            if r < matrix[index][chance]:
                index = words.index(chance)
                break
        out += words[index] + " "
        count += 1
        #RNG breakthrough
        r = random.randint(0, count)
        if r >= 50:
            early = True
            break

    #Remove end word
    if not early:
        out = out[0:len(out) - len(end_word_code) - 1]
    print(out)
    print("Type stop to end this madness. Type anything else to continue.")
    cont = input()
    
