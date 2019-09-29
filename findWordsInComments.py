from prettyPrint import prettyPrint
import json

# searching the file for words


def findWordsInComments(word, fileName):
    with open(f"comments from {fileName}") as commentFile:
        data = json.load(commentFile)
        # print(data)
        # prettyPrint(data)
