import json
import requests
with open('cricketers.json', 'r') as f:
    data = json.load(f)

content = ""
temp = ""
json_file = open('output.json', 'w')
printer = {}
count = 0
for key in data.keys():
    count = count + 1
    print(count, key)
    printer[key] = data[key]
    url = 'https://hi.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&titles='
    url += data[key]['Hindi sitelink'].split('/')[-1]
    try:
        dataframe = requests.get(url).json()
    except:
        continue
    for other_key in dataframe['query']['pages']:
        try:
            content = dataframe['query']['pages'][other_key]['extract']
        except:
            content = "CONTENT WAS NOT FOUND"
    printer[key]['wikipedia content'] = content
json.dump(printer, json_file)