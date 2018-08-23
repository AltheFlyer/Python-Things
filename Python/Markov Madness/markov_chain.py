#MarkovChain.py
#Allen Liu
#August 14, 2018
#########################DESCRIPTION#########################
#A VERY simple markov chain test
#Made to not to be super hardcoded
#Definitely not a Jhin simulator
#############################################################

import random

#To simulate the matrix, let's try a list of dicts
vals = ["one", "two", "three", "FOUR"]
raw_matrix = [{}]

raw_matrix[0] = {vals[0]:0.0, vals[1]:1.0, vals[2]:0.0, vals[3]:0.0}
raw_matrix.append({vals[0]:0.2, vals[1]:0.0, vals[2]:0.8, vals[3]:0.0})
raw_matrix.append({vals[0]:0.2, vals[1]:0.0, vals[2]:0.0, vals[3]:0.8})
raw_matrix.append({vals[0]:1.0, vals[1]:0.0, vals[2]:0.0, vals[3]:0.0})

print(raw_matrix)

#Converts matrix to something suitible for rng
#Each value (sigma) represents what the rng value must be
#below for the index to be chosen
matrix = raw_matrix
for i in range(len(matrix)):
    sigma = 0
    for key in matrix[i]:
        if matrix[i][key] != 0:
            sigma += matrix[i][key]
            print(sigma)
            matrix[i][key] = sigma

for chance in matrix:
    print(chance)

index = 0
out = ""
for i in range(20):
    out += vals[index] + " "
    #The markoving
    r = random.random()
    print(r)
    #A sorta dodgy way of getting the random chances to work
    for chance in matrix[index].keys():
        #Code above will order the values, so
        #the break helps prevent indices from automatically
        #becoming the highest value possible
        if r < matrix[index][chance]:
            index = vals.index(chance)
            break

print(out)  
