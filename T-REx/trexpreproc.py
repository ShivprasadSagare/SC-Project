
import json

with open('re-nlg_0-10000.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# print(data)

# for x in range(data):
print(data[0]);
# print(data[0]['triples'][1]);
# for x in data:
	# print(x['docid']);

# print(data[0]['triples'][1]);