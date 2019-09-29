#!/usr/bin/python
import time
from getData import getData
from getCommentsFromData import getCommentsFromData
from findWordsInComments import findWordsInComments
from printProgressBar import printProgressBar
# the below will be ready when not in dev
# fileName = input("What do you want the file to be called?")
# user = input("What reddit user JSON object do you want to download? ")
fileName = "data.txt"
user = "hello"
url = f"https://www.reddit.com/u/{user}.json"
actions = 5

# getting the data
printProgressBar(0, actions, prefix='Progress:', suffix='Complete',
                 length=50, customString="Getting the Data object")
getData(url, fileName)
printProgressBar(1, actions, prefix='Progress:', suffix='Complete',
                 length=50, customString="Retrived the Data object")

# import data from disk then organize data and clean/munge it
getCommentsFromData(fileName)

# apply requested parameters
# word = input("What word would you like to check for? ")
word = "which"
findWordsInComments(word, fileName)


# save to disk

# print out in graphing library of words and time used
