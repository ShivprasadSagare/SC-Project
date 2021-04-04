# !pip install -U torch
import torch
# !pip install -U transformers
# !pip install -U sentence-transformers
import transformers
from sentence_transformers import SentenceTransformer,util
import numpy as np
from nltk.tokenize import RegexpTokenizer
import re


file = open('hindi.txt', 'r')
book = file.read()

file2 = open('english.txt' , 'r')
book2 = file2.read()

def sentences(book):
    if book is not None:
        senten = re.split("\." , book)
    return senten

h_se = sentences(book);
e_se = sentences(book2);


# model = SentenceTransformer('stsb-xlm-r-multilingual')
# model = SentenceTransformer('distiluse-base-multilingual-cased-v2')
# model = SentenceTransformer('distiluse-base-multilingual-cased-v2')
model = SentenceTransformer('paraphrase-xlm-r-multilingual-v1')


# sentence1 = "I love dogs"sentence2 = "मुझे कुत्ते अच्छे लगते हैं"# encode sentences to get their embeddingsembedding1 = model.encode(sentence1, convert_to_tensor=True)embedding2 = model.encode(sentence2, convert_to_tensor=True)# compute similarity scores of two embeddingscosine_scores = util.pytorch_cos_sim(embedding1, embedding2)print("Sentence 1:", sentence1)print("Sentence 2:", sentence2)print("Similarity score:", cosine_scores.item())


for i in range(0,len(e_se)):
	sentence1 = e_se[i]
	for j in range(0,len(h_se)):
		sentence2 = h_se[j]
		# encode sentences to get their embeddings
		embedding1 = model.encode(sentence1, convert_to_tensor=True)
		embedding2 = model.encode(sentence2, convert_to_tensor=True)
		# compute similarity scores of two embeddings
		cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
		print("Sentence 1:", sentence1)
		print("Sentence 2:", sentence2)
		# if cosine_scores.item()>0.89:
		print("Similarity score:", cosine_scores.item())

