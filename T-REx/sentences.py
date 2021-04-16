import re
import json
import glob
import os


file = open('commonids.txt', 'r')
cid = file.read()

file = open('actors.txt', 'r')
acid = file.read()

file = open('cricketers.txt', 'r')
crid = file.read()

file = open('politicians.txt', 'r')
poid = file.read()

def ids(f):
    if f is not None:
        senten = re.split("\n" , f)
    return senten

cid_tok = ids(cid)

with open('a_c_p.json') as f2:
  data2 = json.load(f2)

def ids(f):
    if f is not None:
        senten = re.split("\n" , f)
    return senten

# c_id = ids(hid)

# print(data2["p"])

for x in range(len(cid_tok)):

	if(cid_tok[x] is not ''):
		
		if(cid_tok[x] in acid):
			print(cid_tok[x])
			print(data2["a"][cid_tok[x]]["sentences"])
		elif(cid_tok[x] in crid):
			print(cid_tok[x])
			print(data2["c"][cid_tok[x]]["sentences"])
		elif(cid_tok[x] in poid):
			print(cid_tok[x])
			print(data2["p"][cid_tok[x]]["sentences"])




# use global hindi data and see homany matches

# Print png images in folder C:\Users\admin\
# eng_id = open(r"en_id.txt","w+")



new_ids = ["0"]
for filepath in glob.iglob(r'TREx/*.json'):
	with open(filepath) as f:
		data = json.load(f)
		for x in range(len(data)):
			for y in range(len(cid_tok)):
				if(cid_tok[y] is not ''):
					# count = 0
					# for z in range(len(new_ids)):
					# 	if(cid_tok[y] != new_ids[z]):
					# 		count = count +1
					# if(count == len(new_ids)):
					# 	new_ids.append(cid_tok[y])
					if('http://www.wikidata.org/entity/'+cid_tok[y] == data[x]['docid']):
						print(cid_tok[y])
						print(data[x]); #gives data the whole
						# print(data[x]['text']); #gives sentences
					# print(data[x]['triples']); #gives sentence triples

					# print(data[x]['entities']);#gives all triples


# http://www.wikidata.org/entity/Q16137319




	# print(cid_tok[x])

# print(typeof(data2))
# print(data2["a"]["Q6448629"]["sentences"])
# print(data2['triples'])
# for x in data2['sentences']:
# 	print(x);
# 	# print(x['entity_id']);
# # # print('.......................................................................................................................');

# for x in data2['cricketers']:
# 	print(x['entity_id']);
# # # print('.......................................................................................................................');

# for x in data2['politicians']:
# 	print(x['entity_id']);
# # # print('.......................................................................................................................');

# # # print(data[0]['triples'][1]);