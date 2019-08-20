#Imprting the requierd packages

from pickle import load
from numpy import argmax
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from nltk.translate.bleu_score import corpus_bleu

#===============================================================================================

#Requierd functionalities

# load a clean dataset
def load_cleaned_sentences(filename):
	return load(open(filename, 'rb'))

#Encoding Text file to numbers =>

# Encoding Using text_to_sequences (Preprocessing.text) and pad_sequences(preprocessing.sequences) both from keras
def creating_tokenizer(lines):
	tokenizer = Tokenizer()
	tokenizer.fit_on_texts(lines)
	return tokenizer

# max sentence length
def max_length(lines):
	return max(len(line.split()) for line in lines)

# encode and pad sequences
def encode_sequences(tokenizer, length, lines):
	# integer encode sequences
	X = tokenizer.texts_to_sequences(lines)
	# pad sequences with 0 values
	X = pad_sequences(X, maxlen=length, padding='post')
	return X

# map an integer to a word
def word_for_id(integer, tokenizer):
	for word, index in tokenizer.word_index.items():
		if index == integer:
			return word
	return None
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Model predicting Functions

# generate target given source sequence
def predict_sequence(model, tokenizer, source):
	prediction = model.predict(source, verbose=0)[0]
	integers = [argmax(vector) for vector in prediction]
	target = list()
	for i in integers:
		word = word_for_id(i, tokenizer)
		if word is None:
			break
		target.append(word)
	return ' '.join(target)

# evaluate the skill of the model
def evaluate_model(model, tokenizer, sources, raw_dataset):
	actual, predicted = list(), list()
	for i, source in enumerate(sources):
		# translate encoded source text
		source = source.reshape((1, source.shape[0]))
		translation = predict_sequence(model, english_tokenizer, source)
		raw_target, raw_src = raw_dataset[i]
		if i < 10:
			print('src=[%s], target=[%s], predicted=[%s]' % (raw_src, raw_target, translation))
		actual.append(raw_target.split())
		predicted.append(translation.split())
	# calculate BLEU score
	print('BLEU-1: %f' % corpus_bleu(actual, predicted, weights=(1.0, 0, 0, 0)))
	#print('BLEU-2: %f' % corpus_bleu(actual, predicted, weights=(0.5, 0.5, 0, 0)))
	#print('BLEU-3: %f' % corpus_bleu(actual, predicted, weights=(0.3, 0.3, 0.3, 0)))
	#print('BLEU-4: %f' % corpus_bleu(actual, predicted, weights=(0.25, 0.25, 0.25, 0.25)))

#=================================================================================================

#Main()
# load datasets
dataset = load_cleaned_sentences('English-Malayalam-both.pkl')
train = load_cleaned_sentences('English-Malayalam-train.pkl')
test = load_cleaned_sentences('ENglish-Malayalam-test.pkl')
# prepare english tokenizer
english_tokenizer = creating_tokenizer(dataset[:, 0])
english_vocab_size = len(english_tokenizer.word_index) + 1
english_length = max_length(dataset[:, 0])
# prepare Malayalam tokenizer
malayalam_tokenizer = creating_tokenizer(dataset[:, 1])
malayalam_vocab_size = len(malayalam_tokenizer.word_index) + 1
malayalam_length = max_length(dataset[:, 1])
# prepare data
trainX = encode_sequences(malayalam_tokenizer, malayalam_length, train[:, 1])
testX = encode_sequences(malayalam_tokenizer, malayalam_length, test[:, 1])

# load model
model = load_model('Malayalam_Model.h5')
# test on some training sequences
for i, source in enumerate(trainX):
		# translate encoded source text
		source = source.reshape((1, source.shape[0]))
prediction = model.predict(source, verbose=0)[0]
print(prediction[:5])
# test on some training sequences

print('train')
evaluate_model(model, english_tokenizer, trainX, train)
# test on some test sequences
print('test')
evaluate_model(model, english_tokenizer, testX, test)

