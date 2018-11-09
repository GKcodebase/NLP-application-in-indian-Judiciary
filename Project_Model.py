#### Imporing Packages

from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize

from statistics import mode

import random
import pickle

### vote class for running Algorithms and determining the confidence

class Vote_(ClassifierI):
    def __init__(self, *classifier):
        self._classifier = classifier

    def classify(self, feature):
        vote = []
        for c in self._classifier:
            v = c.classify(feature)
            vote.append(v)
        return mode(vote)

    def confidence(self, feature):
        vote = []
        for c in self._classifier:
            v = c.classify(feature)
            vote.append(v)

        choice_vote = vote.count(mode(vote))
        confidence_ = choice_vote / len(vote)
        return confidence_


document = open("pickled_algorithms/document.pickle", "rb")
documents = pickle.load(document)
document.close()

word_feature = open("pickled_algorithms/word_features.pickle", "rb")
word_features = pickle.load(word_feature)
word_feature.close()


def find_feature(document):
    word = word_tokenize(document)
    feature = {}
    for w in word_features:
        feature[w] = (w in word)

    return feature

featureset = [(find_feature(rev), category) for (rev, category) in documents]

random.shuffle(featureset)
testing_set = featureset[1400:]
training_set = featureset[:1433]

open_file = open("pickled_algorithms/LinearSVC_classifier.pickle", "rb")
LinearSVC = pickle.load(open_file)
open_file.close()

open_file = open("pickled_algorithms/SGDC_classifier.pickle", "rb")
SGDC = pickle.load(open_file)
open_file.close()


open_file_ = open("pickled_algorithms/naivebayes.pickle", "rb")
naive_bayes = pickle.load(open_file_)
open_file_.close()

open_file = open("pickled_algorithms/MNB_classifier.pickle", "rb")
MNB = pickle.load(open_file)
open_file.close()

open_file = open("pickled_algorithms/BernoulliNB_classifier.pickle", "rb")
BernoulliNB= pickle.load(open_file)
open_file.close()

open_file = open("pickled_algorithms/LogisticRegression_classifier.pickle", "rb")
LogisticRegression = pickle.load(open_file)
open_file.close()

# Making Instance of the class vote
Classify = Vote_(
    LogisticRegression, SGDC,naive_bayes,LinearSVC,MNB,BernoulliNB
            )

def Analayse(text):
    feat = find_feature(text)
    return Classify.classify(feat)
