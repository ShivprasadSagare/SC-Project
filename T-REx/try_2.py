import re
import json
import glob
import os


file = open('commonids.txt', 'r')
cid = file.read()

file2 = open('english_sentences.txt', 'r')
eid = file2.read()

file3 = open('English.txt', 'r')
enid = file3.read()

file4 = open('Hindi.txt', 'r')
hnid = file4.read()


def ids(f):
    if f is not None:
        senten = re.split("\n" , f)
        # senten = re.split("\.\s" , f)
    return senten
def ids2(f):
    if f is not None:
        # senten = re.split("a" , f)
        senten = re.split("\n" , f)
        # senten = re.split("\.\s" , f)
    return senten
cid_tok = ids(cid)
e_id = ids2(eid)
en_id = ids2(enid)
hn_id = ids2(hnid)
# print(e_id[6])

with open('english_data.json') as f2:
  data = json.load(f2)


def findf(sent, dataa ):
	data_a = ids(dataa)
	for x in range(len(data_a)):
		if(sent in data_a[x]):
			return x
		else:
			return "k"

for x in range(len(data["data"])):
	datax = ids(data["data"][x]['text'])

for x in range(len(data["data"])):
	for y in range(len(cid_tok)):
		if(cid_tok[y] is not ''):
			# print(data["data"][x]['docid'])
			# print('http://www.wikidata.org/entity/'+cid_tok[y])
			if('http://www.wikidata.org/entity/'+cid_tok[y] == data["data"][x]['docid']):
				for z in range(len(en_id)):
					# print(e_id[z])
					if(en_id[z] in data["data"][x]['text'] and en_id[z] != ''):
						k = findf(en_id[z],data["data"][x]['text'])
						# print(data["data"][x]['text'])
						for xx in range(len(data["data"][x]['triples'])):
							if(data["data"][x]['triples'][xx]['sentence_id'] == k):
								print("\n")
								print("'sentence':"+hn_id[z])
								# print(data["data"][x]['triples'][xx]['sentence_id'])
								print(data["data"][x]['triples'][xx])
					# print(cid_tok[y])
					# print(data["data"][x]); #gives data the whole
				# print(data["data"][x]['text']); #gives sentences
			# print(data["data"][x]['triples']); #gives sentence triples
			# print(data["data"][x]['entities']);#gives all triples

