# Python program to generate word vectors using Word2Vec

# importing all necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings

warnings.filterwarnings(action = 'ignore')

import gensim
from gensim.models import Word2Vec

import joblib

# Reads ‘train_text.txt’ file. The file contains general information about various domains such as education, healthcare, etc.
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
			temp.append(j.lower()) # We don't need to take purely numerical strings for training the model

	data.append(temp)

# Skip-Gram Model
model = gensim.models.Word2Vec(data, min_count = 1, vector_size = 100,
											window = 5, sg = 1)

# Save trained model using joblib
joblib.dump(model, "prediction_model.joblib")