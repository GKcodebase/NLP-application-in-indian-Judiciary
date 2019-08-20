#Importing the requierd  Packages

import string
import re
from pickle import dump
from unicodedata import normalize
from numpy import array

#=====================================================================================================================================

#Functions Requierd

# load raw_document(English-Malayalam language phrases) into memory
def load_document(file_name):
	# open the file as read only
	file = open(file_name, mode='rt', encoding='utf-8')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

# split a loaded document into sentences pair
def to_Sentence_pairs(doc):
	lines = doc.strip().split('\n')
	pairs = [line.split('\t') for line in  lines]
	return pairs

# clean a list of lines(Removing White spaces,reducing to lowe case ,removing number)
def clean_sentence_pairs(lines):
	cleaned = list()
	# prepare translation table for removing punctuation
	#table = str.maketrans('', '', string.punctuation)
	for pair in lines:
		clean_pair = list()
		for line in pair:
			# tokenize on white space
			line = line.split()
			# convert to lowercase
			line = [word.lower() for word in line]
			# remove punctuation from each token
			#line = [word.translate(table) for word in line]
			# remove tokens with numbers in them
			line = [word for word in line if not word.isnumeric()]
			# store as string
			clean_pair.append(' '.join(line))
		cleaned.append(clean_pair)
	return array(cleaned)

# clean a list of lines
def clean_pairs(lines):
	cleaned = list()
	# prepare regex for char filtering
	re_print = re.compile('[^%s]' % re.escape(string.printable))
	# prepare translation table for removing punctuation
	table = str.maketrans('', '', string.punctuation)
	for pair in lines:
		clean_pair = list()
		for line in pair:
			# normalize unicode characters
			line = normalize('NFD', line).encode('ascii', 'ignore')
			line = line.decode('UTF-8')
			# tokenize on white space
			line = line.split()
			# convert to lowercase
			line = [word.lower() for word in line]
			# remove punctuation from each token
			line = [word.translate(table) for word in line]
			# remove non-printable chars form each token
			line = [re_print.sub('', w) for w in line]
			# remove tokens with numbers in them
			line = [word for word in line if word.isalpha()]
			# store as string
			clean_pair.append(' '.join(line))
		cleaned.append(clean_pair)
	return array(cleaned)

# save a list of clean sentences to file(Pickling the Sentence Pair)
def save_clean_data(sentences, filename):
	dump(sentences, open(filename, 'wb'))
	print('Saved: %s' % filename)

#===============================================================================================

#Main Code

# load raw_dataset
filename = 'complaint letter mal-eng.txt'
document = load_document(filename)
# split into english-malyalam pairs
sentence_pairs = to_Sentence_pairs(document)
# clean sentences
clean_pairs = clean_sentence_pairs(sentence_pairs)
# save clean pairs to file
save_clean_data(clean_pairs, 'English-Malayalam.pkl')
# spot check
for i in range(10):
	print('[%s] => [%s]' % (clean_pairs[i,0], clean_pairs[i,1]))
