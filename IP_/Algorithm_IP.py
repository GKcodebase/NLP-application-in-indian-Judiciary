
###### Import packages
import random
import nltk
from nltk.classify.scikitlearn import SklearnClassifier

from  nltk.stem import  WordNetLemmatizer

from nltk.tokenize import word_tokenize

#### DAtasets
law1 = open("IP/IP83.txt", "r").read()
law2 = open("IP/IP84.txt", "r").read()
law3 = open("IP/IP85.txt", "r").read()
law4 = open("IP/IP86.txt","r").read()
law5 = open("IP/IP87.txt","r").read()
law6 = open("IP/IP88.txt","r").read()
law7 = open("IP/IP89.txt","r").read()
law8 = open("IP/IP90.txt","r").read()
law9 = open("IP/IP91.txt","r").read()
law10 = open("IP/IP92.txt","r").read()
law11 = open("IP/IP93.txt","r").read()
law12 = open("IP/IP94.txt","r").read()




allowed_word_type = ["J","R","V"]
all_word = []
document = []

### tagging all words in law1 as law_1
for p in law1.split('\n'):
    ### Making a tuple out of splited line
    document.append((p, "law_1"))
    ### Tokenizing the tagged line
    word = word_tokenize(p)
    for i in word:
        ### lemmatizing each tokenized words
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
        #### removing stopwords
    law_1 = nltk.pos_tag(word)
    for i in law_1:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

### tagging all words in law2 as law_2

for p in law2.split('\n'):
    document.append((p, "law_2"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_2 = nltk.pos_tag(word)
    for i in law_2:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

###########################################
### tagging all words in law3 as law_3
for p in law3.split('\n'):
    document.append((p, "law_3"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_3 = nltk.pos_tag(word)
    for i in law_3:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())
###########################################
# ### tagging all words in law4 as law_4
for p in law4.split('\n'):
    document.append((p, "law_4"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_4 = nltk.pos_tag(word)
    for i in law_4:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

###########################################
### tagging all words in law5 as law_5
for p in law5.split('\n'):
    document.append((p, "law_5"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_5 = nltk.pos_tag(word)
    for i in law_5:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

###########################################
### tagging all words in law5 as law_5
for p in law6.split('\n'):
    document.append((p, "law_6"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_6 = nltk.pos_tag(word)
    for i in law_6:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

###########################################
### tagging all words in law7 as law_7
for p in law7.split('\n'):
    document.append((p, "law_7"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_7 = nltk.pos_tag(word)
    for i in law_7:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

###########################################
### tagging all words in law8 as law_8


for p in law8.split('\n'):
    document.append((p, "law_8"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_8 = nltk.pos_tag(word)
    for i in law_8:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

###########################################
### tagging all words in law9 as law_9

for p in law9.split('\n'):
    document.append((p, "law_9"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_9 = nltk.pos_tag(word)
    for i in law_9:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

###########################################
### tagging all words in law10 as law_10

for p in law10.split('\n'):
    document.append((p, "law_10"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_10 = nltk.pos_tag(word)
    for i in law_10:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

###########################################
### tagging all words in law11 as law_11

for p in law11.split('\n'):
    document.append((p, "law_11"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_11 = nltk.pos_tag(word)
    for i in law_11:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

###########################################
### tagging all words in law12 as law_12

for p in law12.split('\n'):
    document.append((p, "law_12"))
    word = word_tokenize(p)
    for i in word:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_12 = nltk.pos_tag(word)
    for i in law_12:
        if i[1][0] in allowed_word_type:
            all_word.append(i[0].lower())

###########################################

### every tagged word are tagged in document and pickled
import pickle

save_document = open("pickled_algorithms/document.pickle", "wb")
pickle.dump(document, save_document)
save_document.close()
#### Frequency distribution of tokenized words
all_word = nltk.FreqDist(all_word)

#### Selecting most frequent words as feature set
word_feature = list(all_word.keys())[:3000]
save_word_feature = open("pickled_algorithms/word_features.pickle", "wb")
pickle.dump(word_feature, save_word_feature)
save_word_feature.close()


def Find_feature(document):
    word = word_tokenize(document)

    feature = {}
    for w in word_feature:
        feature[w] = (w in word)

    return feature


featureset = [(Find_feature(r), category) for (r, category) in document]

random.shuffle(featureset)
print(len(featureset))

##### Dividing our preprocessed data into training set and testing set

testing_set = featureset[1000:]
training_set = featureset[:1433]

############ Training and Testing each Algorithm

###### importing classifiers

from sklearn.linear_model import LogisticRegression, SGDClassifier

from sklearn.naive_bayes import MultinomialNB, BernoulliNB

from sklearn.svm import  LinearSVC

############## Stochatic Gradient Descent
SGDC = SklearnClassifier(SGDClassifier())
SGDC.train(training_set)
#print("SGD Classifier accuracy percentage:", nltk.classify.accuracy(SGDC, testing_set) * 100)


save_classifier = open("pickled_algorithms/SGDC_classifier.pickle", "wb")
pickle.dump(SGDC, save_classifier)
save_classifier.close()

######## Naive Bayes
classifier = nltk.NaiveBayesClassifier.train(training_set)
#print(" Naive Bayes  accuracy percentage:", (nltk.classify.accuracy(classifier, testing_set)) * 100)


save_classifier = open("pickled_algorithms/naivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

## linear SVM
LinearSVC = SklearnClassifier(LinearSVC())
LinearSVC.train(training_set)
#print("LinearSVC  accuracy percentage:", (nltk.classify.accuracy(LinearSVC, testing_set)) * 100)

save_classifier = open("pickled_algorithms/LinearSVC_classifier.pickle", "wb")
pickle.dump(LinearSVC, save_classifier)
save_classifier.close()

### Multinomial Naive Bayes
MNB = SklearnClassifier(MultinomialNB())
MNB.train(training_set)
#print("Multinomial  naive bayes accuracy percentage:", (nltk.classify.accuracy(MNB, testing_set)) * 100)

save_classifier = open("pickled_algorithms/MNB_classifier.pickle", "wb")
pickle.dump(MNB, save_classifier)
save_classifier.close()

### Bernoulli naive Bayes
BernoulliNB = SklearnClassifier(BernoulliNB())
BernoulliNB.train(training_set)
#print("Bernoulli naive bayes accuracy percentage:", (nltk.classify.accuracy(BernoulliNB, testing_set)) * 100)

save_classifier = open("pickled_algorithms/BernoulliNB_classifier.pickle", "wb")
pickle.dump(BernoulliNB, save_classifier)
save_classifier.close()

### Logistic Regression
LogisticRegression = SklearnClassifier(LogisticRegression())
LogisticRegression.train(training_set)
#print("LogisticRegression  accuracy percentage:",      (nltk.classify.accuracy(LogisticRegression, testing_set)) * 100)

save_classifier = open("pickled_algorithms/LogisticRegression_classifier.pickle", "wb")
pickle.dump(LogisticRegression, save_classifier)
save_classifier.close()



