import json
from datetime import datetime


def getCommentsFromData(fileName):
    comments = []
    with open(fileName) as json_file:
        data = json.load(json_file)
        for data in (data["data"]['children']):
            date = datetime.utcfromtimestamp(
                data['data']["created"]).strftime('%Y%m%d')
            comments.append({date: data['data']["body"]})
            with open(f"comments from {fileName}", 'w') as outfile:
                json.dump(comments, outfile)
