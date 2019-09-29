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
actions = 8

# getting the data
printProgressBar(0, actions, prefix='Progress:', suffix='Complete',
                 length=100, customString=f"Getting the Data object for '{user}'")
time.sleep(0.1)
getData(url, fileName)
time.sleep(0.1)
printProgressBar(1, actions, prefix='Progress:', suffix='Complete',
                 length=100, customString="Retrieved and saved the Data object to the hard disk")
time.sleep(0.1)


# import data from disk then organize data and clean/munge it
printProgressBar(2, actions, prefix='Progress:', suffix='Complete',
                 length=100, customString="Retrieved the saved Data object")
time.sleep(0.1)
getCommentsFromData(fileName)
time.sleep(0.1)
printProgressBar(3, actions, prefix='Progress:', suffix='Complete',
                 length=100, customString="filtered and munged the Data object")
time.sleep(0.1)

# apply requested parameters
# word = input("What word would you like to check for? ")
word = "which"
printProgressBar(4, actions, prefix='Progress:', suffix='Complete',
                 length=100, customString="Received requested word to find")
time.sleep(0.1)
findWordsInComments(word, fileName)
time.sleep(0.1)
printProgressBar(5, actions, prefix='Progress:', suffix='Complete',
                 length=100, customString="Applied word filter")
time.sleep(0.1)

# save to disk
printProgressBar(6, actions, prefix='Progress:', suffix='Complete',
                 length=100, customString="saving data to new file")
time.sleep(0.1)
# apply saving here
time.sleep(0.1)
printProgressBar(7, actions, prefix='Progress:', suffix='Complete',
                 length=100, customString="file saved")
time.sleep(0.1)

# print out in graphing library of words and time used
printProgressBar(8, actions, prefix='Progress:', suffix='Complete',
                 length=100, customString="Printing out data to new graph file")
time.sleep(0.1)
# apply printing here
time.sleep(0.1)
