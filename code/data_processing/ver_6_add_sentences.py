import json
print("shiv")
with open(r"D:\College\research\indic_wikibot\SC_project\SC-Project\data\ver 6\actors.json", encoding='utf8') as file:
    data1 = json.load(file)

with open(r"D:\College\research\indic_wikibot\SC_project\SC-Project\data\ver 3\final_actors.json", encoding='utf8') as file:
    data2 = json.load(file)

keys = list(data1.keys())
for id in keys:
    if(id in data2.keys()):
        data1[id]['sentences'] = data2[id]['sentences']
        triples = []
        personLabel = data1[id]['personLabel']
        for item in data1[id]['triples']:
            triples.append((personLabel, item['propertyLabel'], item['objectLabel']))
        
        data1[id]['triples'] = triples
    else:
        del data1[id]

with open(r"D:\College\research\indic_wikibot\SC_project\SC-Project\data\ver 6\actors.json", 'w') as file:
    json.dump(data1, file)