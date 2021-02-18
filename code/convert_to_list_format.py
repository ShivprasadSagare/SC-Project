from pathlib import Path
import json
from tqdm import tqdm

base_dir = Path(r"D:\College\research\indic_wikibot\SC_project\SC-Project")
read_file_path = Path.joinpath(base_dir, 'data', 'ver 3', 'final_politicians.json')
write_file_path = Path.joinpath(base_dir, 'data', 'ver 4', 'politicians.json')

data = json.load(read_file_path.open())

with tqdm(list(data.keys()), desc='entities converted') as pbar:
    for key in pbar:
        triples = []
        personLabel = data[key]['personLabel']
        for item in data[key]['triples']:
            triples.append((personLabel, item['propertyLabel'], item['objectLabel']))
        
        data[key]['triples'] = triples

with open(write_file_path, 'w') as write_file:
    json.dump(data, write_file)