#Chrome.py
#Opens chrome windows (ideally) based on a config file
#Any links in the file will be opened in the default browser
#Allen Liu
#May the forth 2017

#import stuffs
import webbrowser
import os.path

#Variables
#Index of comment in string
comment = 0;
    
#Open target file
reader = open("ChromeReadFile.txt", "r+")

#Generate list of each line in the file
List = reader.readlines()

#For each line...
for line in List:
    #Remove all spaces
    line = line.replace(" ", "")

    #Ignore this line if it is now blank
    if line == "":
        continue

    #Find any comments
    comment = line.find('#')

    #Set value of line to not include comments
    line = line[0:comment]

    #Open link in browser
    webbrowser.open(line)
    
#close file
reader.close()
