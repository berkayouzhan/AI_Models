# -*- coding: utf-8 -*-
"""natural_language_processing.ipynb adlı not defterinin kopyası

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ebz0htLRnH7OPmmbCrZqM_FfyuppmvvO

# Natural Language Processing

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

"""## Cleaning the texts"""

import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0,1000):
  review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  all_stopwords.remove("didn't")
  all_stopwords.remove("wasn't")
  all_stopwords.remove("no")
  review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
  review = ' '.join(review)
  corpus.append(review)

"""## Creating the Bag of Words model"""

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features= 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

len(X[0])

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

"""## Training the Naive Bayes model on the Training set"""

from sklearn.svm import SVC
classifier= SVC(kernel='linear',random_state=42)
classifier.fit(X_train, y_train)

"""## Predicting the Test set results"""

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""## Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)