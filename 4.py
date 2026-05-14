

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

import nltk
nltk.download('punkt_tab')

nltk.download('stopwords')

import nltk
nltk.download('averaged_perceptron_tagger_eng')

text = "Artificial Intelligence and Machine Learning are important technologies in modern computer science."
print("Original Text:\n", text)

tokens = word_tokenize(text)
print("\nTokens:\n", tokens)

freq = Counter(tokens)
print("\nWord Frequency:\n", freq)

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word.lower() not in stop_words]
print("\nAfter Removing Stopwords:\n", filtered_words)

pos_tags = nltk.pos_tag(filtered_words, lang="eng")
print("\nPOS Tagging:\n", pos_tags)

