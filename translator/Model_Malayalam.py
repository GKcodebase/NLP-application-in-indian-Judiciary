#IMporting the reqiuerd Libraries

from pickle import load
from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Embedding
from keras.layers import RepeatVector
from keras.layers import TimeDistributed
from keras.callbacks import ModelCheckpoint

#======================================================================================

#Requierd Functionalities

# load the cleaned dataset
def load_cleaned_sentences(file_name):
	return load(open(file_name, 'rb'))

# Creating and fiting Tokenizer with Text preprocessing API from keras
def create_tokenizer(lines):
	tokenizer = Tokenizer()
	tokenizer.fit_on_texts(lines)
	return tokenizer

# max sentence length
def max_length(lines):
	return max(len(line.split()) for line in lines)

#Encoding Text file to numbers =>

# Encoding Using text_to_sequences (Preprocessing.text) and pad_sequences(preprocessing.sequences) both from keras
def encoding_sequences(tokenizer, length, lines):
	# integer encode sequences
	X = tokenizer.texts_to_sequences(lines)
	# pad sequences with 0 values
	X = pad_sequences(X, maxlen=length, padding='post')
	return X

# one hot encode target sequence
def encoding_output(sequences, vocab_size):
	ylist = list()
	for sequence in sequences:
		encoded = to_categorical(sequence, num_classes=vocab_size)
		ylist.append(encoded)
	y = array(ylist)
	y = y.reshape(sequences.shape[0], sequences.shape[1], vocab_size)
	return y

# define Nueral Machine Translation model
def define_model(src_vocab, tar_vocab, src_timesteps, tar_timesteps, n_units):
	model = Sequential()
	model.add(Embedding(src_vocab, n_units, input_length=src_timesteps, mask_zero=True))
	model.add(LSTM(n_units))
	model.add(RepeatVector(tar_timesteps))
	model.add(LSTM(n_units, return_sequences=True))
	model.add(TimeDistributed(Dense(tar_vocab, activation='softmax')))
	return model

#===============================================================================================

#Main()


# load datasets

dataset = load_cleaned_sentences('English-Malayalam-both.pkl')
train = load_cleaned_sentences('English-Malayalam-train.pkl')
test = load_cleaned_sentences('English-Malayalam-test.pkl')

# prepare english tokenizer

english_tokenizer = create_tokenizer(dataset[:, 0])
print(dataset[:5])
english_vocab_size = len(english_tokenizer.word_index) + 1
english_length = max_length(dataset[:, 0])
print('English Vocabulary Size: %d' % english_vocab_size)
print('English Max Length: %d' % (english_length))

# prepare Malayalam tokenizer

malayalam_tokenizer = create_tokenizer(dataset[:, 1])
print("#"*25)
malayalam_vocab_size = len(malayalam_tokenizer.word_index) + 1
malayalam_length = max_length(dataset[:, 1])
print('Malayalam Vocabulary Size: %d' % malayalam_vocab_size)
print('Malayalam Max Length: %d' % (malayalam_length))

# prepare training data

trainX = encoding_sequences(malayalam_tokenizer, malayalam_length, train[:, 1])
trainY = encoding_sequences(english_tokenizer, english_length, train[:, 0])
trainY = encoding_output(trainY, english_vocab_size)

# prepare validation data

testX = encoding_sequences(malayalam_tokenizer, malayalam_length, test[:, 1])
testY = encoding_sequences(english_tokenizer, english_length, test[:, 0])
testY = encoding_output(testY, english_vocab_size)

# define model

model = define_model(malayalam_vocab_size, english_vocab_size, malayalam_length, english_length, 64)
model.compile(optimizer='adam', loss='categorical_crossentropy')

# summarize defined model

print(model.summary())

# fit model

filename = 'Malayalam_Model.h5'
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
model.fit(trainX, trainY, epochs=1500, batch_size=64, validation_data=(testX, testY), callbacks=[checkpoint], verbose=2)
