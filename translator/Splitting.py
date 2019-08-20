#Importing the requierd Dataset
from pickle import load
from pickle import dump
from numpy.random import shuffle

#=======================================================================================================

#Requierd Functions

# load the cleaned dataset
def load_cleaned_sentences(file_name):
	return load(open(file_name, 'rb'))

# save a list of clean sentences to file
def save_cleaned_data(sentences, file_name):
	dump(sentences, open(file_name, 'wb'))
	print('Saved: %s' % file_name)

#==========================================================================================================

#Main Function

# load dataset
raw_dataset = load_cleaned_sentences('English-Malayalam.pkl')


# reduce dataset size
print(len(raw_dataset))
n_sentences = 557
dataset = raw_dataset[:n_sentences, :]

# random shuffle
shuffle(dataset)
# split into train/test
train, test = dataset[:557], dataset[200:]
# save
save_cleaned_data(dataset, 'English-Malayalam-both.pkl')
save_cleaned_data(train, 'English-Malayalam-train.pkl')
save_cleaned_data(test, 'English-Malayalam-test.pkl')

