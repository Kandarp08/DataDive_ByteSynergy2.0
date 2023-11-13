# Python program to generate word vectors using Word2Vec

# importing all necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action = 'ignore')

import gensim
from gensim.models import Word2Vec

import joblib

# Reads ‘train_text.txt’ file
sample = open("train_text.txt")
s = sample.read()

# Replaces escape character with space
f = s.replace("\n", " ")

data = []

# iterate through each sentence in the file
for i in sent_tokenize(f):
	temp = []
	
	# tokenize the sentence into words
	for j in word_tokenize(i):
		
		try:
			float(j)

		except:
			temp.append(j.lower())

	data.append(temp)

# # Create CBOW model
# model1 = gensim.models.Word2Vec(data, min_count = 1, 
# 							vector_size = 100, window = 5)

# # Print results
# print("Cosine similarity between 'alice' " +
# 			"and 'wonderland' - CBOW : ",
# 	model1.wv.similarity('alice', 'wonderland'))
	
# print("Cosine similarity between 'alice' " +
# 				"and 'machines' - CBOW : ",
# 	model1.wv.similarity('alice', 'machines'))

# Create Skip Gram model
model2 = gensim.models.Word2Vec(data, min_count = 1, vector_size = 100,
											window = 5, sg = 1)

joblib.dump(model2, "prediction_model.joblib")