import requests
import json

# printing it nice and pretty
def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing),
                         sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


# making the request
def getData(url):
    data = requests.get(url,
                        headers={'User-agent': 'zachsBot1'}).json()

    pp_json(data)
    # writing to a file, and creating if it doesnt exist
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

    # reading from file
    with open('data.txt') as json_file:
        # regular json
        data = json.load(json_file)
        # reddit specific cut
        # data = json.load(json_file)["data"]["children"][0:1]
        pp_json(data)
