#MarkovChainMKII.py
#Allen Liu
#August 14, 2018
#########################DESCRIPTION#########################
#A less simple chain
#The combination of file reading and markov chaining
#Creates a 'database' for each word saved, with values of
#the occurances of another word coming after it
#############################################################

import os.path

#Fills a dict with useless info, that can be modified later
def fill_empty_matrix(words):
    empty_dict = {}
    for word in words:
        empty_dict[word] = 0
    return empty_dict
        
#Get a list of all of the words used.
reader = open("read.txt", "r")
words = []
full_text = []
raw_matrix = []
#Used to show start of a text
start_word_code = "qwertyuiopasdfghjklzxcvbnm"
#Used to show the end of a text
end_word_code = "mnbvcxzlkjhgfdsapoiuytrewq"

lines = reader.readlines()
reader.close()

for line in lines:
    for word in line.split():
        full_text.append(word)
        if not (word in words):
            words.append(word)

#Add in start and end codes
words.append(start_word_code)
words.append(end_word_code)
word_max = len(words)
  
#Now to make the raw matrix.
#Generate the empty matrix first:
#This mess is the only way i know to prevent pointers
for word in words:
    raw_matrix.append(fill_empty_matrix(words))
    
#Finds how many times the word in a is followed by word b
length = len(full_text)
for i in range(length):
    now = full_text[i]
    #Last word check
    if (i + 1 == len(full_text)):
        raw_matrix[words.index(now)][words[word_max - 1]] += 1
    #First word check
    elif (i == 0):
        raw_matrix[word_max - 2][now] += 1
    else:
        raw_matrix[words.index(now)][full_text[i + 1]] += 1


#print(words)
#for i in range(len(words) - 2):
    #print(raw_matrix[i])

#print("Starting words:")
#print(raw_matrix[len(raw_matrix) - 2])

#Read from storage
#Now to do the exact same thing all over again.
#The first line has the list of n words
#Next n lines have markov data.
markov_data = open("markov.txt", "r")
lines = markov_data.readlines()
markov_data.close()
stored_words = []
stored_matrix = []
all_words = []
full_matrix = []

for word in lines[0].split():
    if not (word in stored_words):
        stored_words.append(word)

del lines[0]

for line in lines:
    tmp_dict = {}
    values = line.split()
    for i in range(len(stored_words)):
        tmp_dict[stored_words[i]] = int(values[i])
    stored_matrix.append(tmp_dict)

#print()
#print(stored_words)
#for i in range(len(stored_words) - 2):
    #print(stored_matrix[i])

#print("Starting words:")
#print(stored_matrix[len(stored_matrix) - 2])

#Temporarily remove beginning and ending values
del stored_words[len(stored_words) - 2:len(stored_words)]
del words[len(words) - 2:len(words)]

#Combining everything
for word in words:
    if not (word in all_words):
        all_words.append(word)
        
for word in stored_words:
    if not (word in all_words):
        all_words.append(word)

#Readd the things
all_words.append(start_word_code)
all_words.append(end_word_code)
words.append(start_word_code)
words.append(end_word_code)
stored_words.append(start_word_code)
stored_words.append(end_word_code)

#Create the final matrix
for word in all_words:
    tmp_dict = fill_empty_matrix(all_words)
    new_dict = {}
    old_dict = {}
    #Get markov values from storage and text
    if word in words:
        new_dict = raw_matrix[words.index(word)]
    if word in stored_words:
        old_dict = stored_matrix[stored_words.index(word)]
    for key in new_dict.keys():
        tmp_dict[key] = tmp_dict[key] + new_dict[key]
    for key in old_dict.keys():
        tmp_dict[key] = tmp_dict[key] + old_dict[key]
    full_matrix.append(tmp_dict)

#print()
#print(all_words)
#for i in range(len(all_words) - 2):
    #print(full_matrix[i])

#print("Starting words:")
#print(full_matrix[len(full_matrix) - 2])

#Writing to the dictionary:
writer = open("markov.txt", "w")
#List of words
word_list = ""
for word in all_words:
    word_list += word + " "
writer.write(word_list + "\n")
#Matrix output:
for d in full_matrix:
    out_dict = ""
    for key in d.keys():
        out_dict += str(d[key]) + " "
    writer.write(out_dict + "\n")

writer.close()
