
###### Import packages
import random
import nltk
from  nltk.stem import  WordNetLemmatizer
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.tokenize import word_tokenize

#### DAtasets
law1 = open("Laws/ATTRIBUTION, ACKNOWLEDGMENT AND DESPATCH OF ELECTRONIC RECORDS.txt", "r").read()
law2 = open("Laws/Digital Signature.txt", "r").read()
law3 = open("Laws/DUTIES OF SUBSCRIBERS.txt", "r").read()
law4 = open("Laws/ELECTRONIC GOVERNANCE.txt","r").read()
law5 = open("Laws/ELECTRONIC SIGNATURE CERTIFICATES.txt","r").read()
law6 = open("Laws/INTERMEDIARIES NOT TO BE LIABLE IN CERTAIN CASES.txt","r").read()
law7 = open("Laws/EXAMINER OF ELECTRONIC EVIDENCE.txt","r").read()
law8 = open("Laws/MISCELLANEOUS.txt","r").read()
law9 = open("Laws/NETWORK SERVICE PROVIDERS NOT TO BE LIABLE IN CERTAIN CASES.txt","r").read()
law10 = open("Laws/OFFENCES.txt","r").read()
law11 = open("Laws/PENALTIES AND ADJUDICATION.txt","r").read()
law12 = open("Laws/REGULATION OF CERTIFYING AUTHORITIES.txt","r").read()
law13 = open("Laws/SECURE ELECTRONIC RECORDS AND SECURE DIGITAL SIGNATURES.txt","r").read()
law14 = open("Laws/THE CYBER REGULATIONS APPELLATE TRIBUNAL.txt","r").read()



allowed_word_type = ["J","R","V"]
all_word = []
document = []

### tagging all words in law1 as law_1
for p in law1.split('\n'):
    ### Making a tuple out of splited line
    document.append((p, "law_1"))
    ### Tokenizing the tagged line
    words = word_tokenize(p)
    for i in words:
        ### lemmatizing each tokenized words
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
        #### removing stopwords
    law_1 = nltk.pos_tag(words)
    for w_ in law_1:
        if w_[1][0] in allowed_word_type:
            all_word.append(w_[0].lower())

### tagging all words in law2 as law_2

for p in law2.split('\n'):
    document.append((p, "law_2"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_2 = nltk.pos_tag(words)
    for w in law_2:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################
### tagging all words in law3 as law_3
for p in law3.split('\n'):
    document.append((p, "law_3"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_3 = nltk.pos_tag(words)
    for w in law_3:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())
###########################################
# ### tagging all words in law4 as law_4
for p in law4.split('\n'):
    document.append((p, "law_4"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_4 = nltk.pos_tag(words)
    for w in law_4:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################
### tagging all words in law5 as law_5
for p in law5.split('\n'):
    document.append((p, "law_5"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_5 = nltk.pos_tag(words)
    for w in law_5:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################
### tagging all words in law5 as law_5
for p in law6.split('\n'):
    document.append((p, "law_6"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_6 = nltk.pos_tag(words)
    for w in law_6:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################
### tagging all words in law7 as law_7
for p in law7.split('\n'):
    document.append((p, "law_7"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_7 = nltk.pos_tag(words)
    for w in law_7:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################

for p in law8.split('\n'):
    document.append((p, "law_8"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_8 = nltk.pos_tag(words)
    for w in law_8:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################

for p in law9.split('\n'):
    document.append((p, "law_9"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_9 = nltk.pos_tag(words)
    for w in law_9:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################

for p in law10.split('\n'):
    document.append((p, "law_10"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_10 = nltk.pos_tag(words)
    for w in law_10:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################

for p in law11.split('\n'):
    document.append((p, "law_11"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_11 = nltk.pos_tag(words)
    for w in law_11:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################

for p in law12.split('\n'):
    document.append((p, "law_12"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_12 = nltk.pos_tag(words)
    for w in law_12:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################

for p in law13.split('\n'):
    document.append((p, "law_13"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_13 = nltk.pos_tag(words)
    for w in law_13:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

###########################################

for p in law14.split('\n'):
    document.append((p, "law_14"))
    words = word_tokenize(p)
    for i in words:
        lemmatizer = WordNetLemmatizer()
        lemmatizer.lemmatize(i)
    law_14 = nltk.pos_tag(words)
    for w in law_14:
        if w[1][0] in allowed_word_type:
            all_word.append(w[0].lower())

### every tagged word are tagged in document and pickled
import pickle

save_document = open("pickled_algorithms/document.pickle", "wb")
pickle.dump(document, save_document)
save_document.close()
#### Frequency distribution of tokenized words
all_words = nltk.FreqDist(all_word)

#### Selecting most frequent words as feature set
word_feature = list(all_words.keys())[:3000]
save_word_features = open("pickled_algorithms/word_features.pickle", "wb")
pickle.dump(word_feature, save_word_features)
save_word_features.close()


def find_feature(document):
    words = word_tokenize(document)

    feature = {}
    for w in word_feature:
        feature[w] = (w in words)

    return feature


featureset = [(find_feature(r), category) for (r, category) in document]

random.shuffle(featureset)

##### Dividing our preprocessed data into training set and testing set

testing_set = featureset[1000:]
training_set = featureset[:1433]

############ Training and Testing each Algorithm

###### importing classifiers

from sklearn.linear_model import LogisticRegression, SGDClassifier

from sklearn.naive_bayes import MultinomialNB, BernoulliNB

from sklearn.svm import  LinearSVC


SGDC = SklearnClassifier(SGDClassifier())
SGDC.train(training_set)
print("SGD Classifier accuracy percentage:", nltk.classify.accuracy(SGDC, testing_set) * 100)

save_classifier = open("pickled_algorithms/SGDC_classifier.pickle", "wb")
pickle.dump(SGDC, save_classifier)
save_classifier.close()

classifier = nltk.NaiveBayesClassifier.train(training_set)
print(" Naive Bayes  accuracy percentage:", (nltk.classify.accuracy(classifier, testing_set)) * 100)


save_classifier = open("pickled_algorithms/naivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

LinearSVC = SklearnClassifier(LinearSVC())
LinearSVC.train(training_set)
print("LinearSVC  accuracy percentage:", (nltk.classify.accuracy(LinearSVC, testing_set)) * 100)

save_classifier = open("pickled_algorithms/LinearSVC_classifier.pickle", "wb")
pickle.dump(LinearSVC, save_classifier)
save_classifier.close()

MNB = SklearnClassifier(MultinomialNB())
MNB.train(training_set)
print("Multinomial  naive bayes accuracy percentage:", (nltk.classify.accuracy(MNB, testing_set)) * 100)

save_classifier = open("pickled_algorithms/MNB_classifier.pickle", "wb")
pickle.dump(MNB, save_classifier)
save_classifier.close()

BernoulliNB = SklearnClassifier(BernoulliNB())
BernoulliNB.train(training_set)
print("Bernoulli naive bayes accuracy percentage:", (nltk.classify.accuracy(BernoulliNB, testing_set)) * 100)

save_classifier = open("pickled_algorithms/BernoulliNB_classifier.pickle", "wb")
pickle.dump(BernoulliNB, save_classifier)
save_classifier.close()

LogisticRegression = SklearnClassifier(LogisticRegression())
LogisticRegression.train(training_set)
print("LogisticRegression  accuracy percentage:",
      (nltk.classify.accuracy(LogisticRegression, testing_set)) * 100)

save_classifier = open("pickled_algorithms/LogisticRegression_classifier.pickle", "wb")
pickle.dump(LogisticRegression, save_classifier)
save_classifier.close()



