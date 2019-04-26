#Importing the requierd database

from  nltk.stem import  WordNetLemmatizer
import nltk
from nltk.tokenize import word_tokenize



data = []
all_word = []
#allowed word set in the processed dataset
allowed_word_type = ["J","R","V"]

#Teading in and preprocessing the raw data
file = open("data.txt","r").read()
for p in file.split('.'):
    ### Making a tuple out of splited line
    data.append((p))
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

#Uncomment to see dataset and words
#print(data[:10])
#print(all_word[:10])

#Importing Requierd packages from sklearn
from sklearn.decomposition import NMF, LatentDirichletAllocation, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer

#Inputing requierd number of topics as the system cann't divide it by itself
NUM_TOPICS = 14

#CountVectorizer for the dataset
Vectorizer = CountVectorizer(min_df=5, max_df=0.9,
                             stop_words='english', lowercase=True,
                             token_pattern='[a-zA-Z\-][a-zA-Z\-]{2,}')

data_vectorized = Vectorizer.fit_transform(data)

# Build a Latent Dirichlet Allocation Model
lda_model = LatentDirichletAllocation(n_topics=NUM_TOPICS, max_iter=10, learning_method='online')
lda_Z = lda_model.fit_transform(data_vectorized)
#Uncoment to see document number and toic number
#print(lda_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)

# Build a Non-Negative Matrix Factorization Model
nmf_model = NMF(n_components=NUM_TOPICS)
nmf_Z = nmf_model.fit_transform(data_vectorized)
#Uncoment to see document number and toic number
#print(nmf_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)

# Build a Latent Semantic Indexing Model
lsi_model = TruncatedSVD(n_components=NUM_TOPICS)
lsi_Z = lsi_model.fit_transform(data_vectorized)
#Uncoment to see document number and toic number
#print(lsi_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)
# Uncomment to visualize how the first document in the corpus looks like in different topic spaces
#print(lda_Z[0])
#print(nmf_Z[0])
#print(lsi_Z[0])

#Function to print topic in every model

def print_topics(model, vectorizer, top_n=10):
    for idx, topic in enumerate(model.components_):
        print("Topic %d:" % (idx))
        print([(vectorizer.get_feature_names()[i], topic[i])
               for i in topic.argsort()[:-top_n - 1:-1]])

#Uncomment to see the Model Visulaization of the Model
"""
print("LDA Model:")
print_topics(lda_model, Vectorizer)
print("=" * 20)

print("NMF Model:")
print_topics(nmf_model, Vectorizer)
print("=" * 20)

print("LSI Model:")
print_topics(lsi_model, Vectorizer)
print("=" * 20)
"""

#Keeping the Contents of complaint letter as Model input

text = " abusive comment on social media by the accused person named below who has posted offensive comment on social media against me through computer resource/ (Mobile Phone) which is grossly offensive and has menacing character. The said person very well knows that such information is false and has posted the same for the purpose of causing annoyance, inconvenience, danger, obstruction, insult, injury, criminal intimidation, enmity, hatred and ill will. He is persistently doing such acts by making use of computer resource and communication device (Mobile) for sending such message.The said person has circulated the said offensive and false material on the internet which is visible at (give the details of the web portal or platform where the message has been posted). The offensive material is not only false but frivolous, defamatory, abusive and insinuative and has been done with the intention to insult and libel me and cause a scandal by slandering and slurring my character. This amounts to making defamatory comment on social media and several persons have already asked me about the same believing the same to be true. This has been done with the intention to defame and injure my character and reputation and cause injury to my character. The aforesaid person is liable for prosecution for offensive comment on social media and other offenses. I request you to take legal action against the said person at the earliest."
x = nmf_model.transform(Vectorizer.transform([text]))[0]
print(x)

y = lsi_model.transform(Vectorizer.transform([text]))[0]
print(y)

import pyLDAvis.sklearn
visualisation = pyLDAvis.sklearn.prepare(lda_model, data_vectorized, Vectorizer)
pyLDAvis.save_html(visualisation, 'LDA_Visualization.html')

import gensim
visualisation = pyLDAvis.gensim.prepare(lda_model, data_vectorized, Vectorizer)
pyLDAvis.save_html(visualisation, 'LDA_Visualization.html')

