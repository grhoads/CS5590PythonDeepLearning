import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

#QUESTION 1:

#read in csv
df = pd.read_csv('cars.csv')

#split into 2 different sets randomly
df['split'] = np.random.randn(df.shape[0], 1)
msk = np.random.rand(len(df)) <= 0.7

#Assign training and test data
train = df[msk]
test = df[~msk]

#handle categorical data
train=train.apply(LabelEncoder().fit_transform)
test=train.apply(LabelEncoder().fit_transform)

#assign train_x, train_y, and test_x the correct columns
X_train = train.drop(" brand", axis=1)
Y_train = train[" brand"]
X_test = test.drop(" brand",axis=1)

#apply SVM algorithm and print accuracy
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
print("svm accuracy is:", acc_svc)

#apply KNN algorithm and print accuracy
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)
print("KNN accuracy is:",acc_knn)

#apply GAUSS algorithm and print accuracy
kernel = 1.0 * RBF(1.0)
gpc = GaussianProcessClassifier(kernel=kernel, random_state=0)
gpc.fit(X_train, Y_train)
Y_pred = gpc.predict(X_test)
gnb_acc = round(gpc.score(X_train, Y_train) * 100, 2)
print("GAUSSIAN accuracy is:",gnb_acc)


#QUESTION 3:
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
import operator

#read in text file
text = open('nlp_input.txt', "r").read()

#tokenize text file by word and print
tokenize =  nltk.word_tokenize(text)
print(tokenize)

#initialize lemmatizer and print out every word and it's lematized version
lemmatizer = WordNetLemmatizer()
for word in tokenize:
    print(word)
    print(lemmatizer.lemmatize(word))

# initialize trigrams and dictionary of trigrams and count
trigramDict = {}
trigrams = ngrams(tokenize, 3)

# for trigram in list of all trigrams
for words in trigrams:
    #if the trigram isn't in our dictionary...
    if words not in trigramDict:
        #add it to our dictionary and initialize count to 1
        trigramDict[words] = 1
    #otherwise if it is in our dictionary...
    else:
        #add 1 to its count
        trigramDict[words] += 1

#initialize list of ten most used trigrams
tenTri = []

#sort dictionary of trigrams by most used in descending order
sorted_d = sorted(trigramDict.items(), key=operator.itemgetter(1), reverse= True)

#add the top 10 most used trigrams to our list
for x in range(0, 10):
    print(sorted_d[x])
    tenTri.append(sorted_d[x][0])

#tokenize the text file by sentence
tokenSent =  nltk.sent_tokenize(text)

#convert the trigrams from tuples to 1 string
triStr = []
for tri in tenTri:
    triStr.append(tri[0]+ ' ' + tri[1] + ' ' + tri[2])

#initialize dictionary of sentences that have the most trigrams in them
mostTriSent = {}

#for each sentence in our tokenized sentences...
for sent in tokenSent:
    #for each trigram string...
    for x in triStr:
        #if the trigram string is in our sentence...
        if x in sent:
            #and if that sentence isn't in our dictionary...
            if sent not in mostTriSent:
                #add the sentence to our dictionary and initialize its count to 1
                mostTriSent[sent] = 1
            #otherwise if it is in our dictionry...
            else:
                #increment its count by 1
                mostTriSent[sent] +=1

#sort our dictionary by value in descending order
sorted_t = sorted(mostTriSent.items(), key=operator.itemgetter(1), reverse= True)

#append each sentence in our sorted dictionary to one another
concat = ""
for x in sorted_t:
    concat += x[0] + " "

#print the sentences out
print(concat)