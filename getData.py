import requests
import json

# making the request


def getData(url, fileName):
    data = requests.get(url,
                        headers={'User-agent': 'zachsBot1'}).json()
    # writing to a file, and creating if it doesnt exist
    with open(fileName, 'w') as outfile:
        json.dump(data, outfile)
