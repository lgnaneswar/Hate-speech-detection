#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the packages
import pandas as pd
import numpy as np
from sklearn. feature_extraction. text import CountVectorizer
from sklearn. model_selection import train_test_split
from sklearn. tree import DecisionTreeClassifier


# In[2]:


import nltk
import re
#nltk. download('stopwords')
from nltk. corpus import stopwords
stopword=set(stopwords.words('english'))
stemmer = nltk. SnowballStemmer("english")


# In[5]:


data = pd. read_csv("twitter.csv")
#To preview the data
print(data. head())


# In[6]:


data["labels"] = data["class"]. map({0: "Hate Speech", 1: "Offensive Speech", 2: "No Hate and Offensive Speech"})
data = data[["tweet", "labels"]]
print(data. head())


# In[12]:


import string


# In[13]:


def clean (text):
 text = str (text). lower()
 text = re. sub('[.?]', '', text) 
 text = re. sub('https?://\S+|www.\S+', '', text)
 text = re. sub('<.?>+', '', text)
 text = re. sub('[%s]' % re. escape(string.punctuation), '', text)
 text = re. sub('\n', '', text)
 text = re. sub('\w\d\w', '', text)
 text = [word for word in text.split(' ') if word not in stopword]
 text=" ". join(text)
 text = [stemmer. stem(word) for word in text. split(' ')]
 text=" ". join(text)
 return text
data["tweet"] = data["tweet"]. apply(clean)


# In[14]:


x = np. array(data["tweet"])
y = np. array(data["labels"])
cv = CountVectorizer()
X = cv. fit_transform(x)
# Splitting the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[15]:


#Model building
model = DecisionTreeClassifier()
#Training the model
model. fit(X_train,y_train)


# In[16]:


#Testing the model
y_pred = model. predict (X_test)
y_pred


# In[17]:


#Accuracy Score of our model
from sklearn. metrics import accuracy_score
print (accuracy_score (y_test,y_pred))


# In[23]:


#Predicting the outcome
inp = "You are too bad and I dont like your attitude,fuck you"
inp = cv.transform([inp]).toarray()
print(model.predict(inp))


# In[26]:


inp = "It is really awesome"
inp = cv. transform([inp]). toarray()
print(model. predict(inp))


# In[ ]:




