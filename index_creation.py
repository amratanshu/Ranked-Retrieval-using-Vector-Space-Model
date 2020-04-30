import collections
import math
from bs4 import BeautifulSoup
import nltk

from nltk import FreqDist
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
# import numpy as np
import string

# import matplotlib.pyplot as plt


# In[2]:


ag40 = open('wiki_40', encoding="utf8")

soup = BeautifulSoup(ag40, 'lxml')


# In[3]:


docList = soup.findAll('doc')
numberDocs = len(docList)
docs = []

for i in range(numberDocs):
    soupTemp = BeautifulSoup(str(docList[i]))
    txtTemp = soupTemp.get_text()
    docs.append(txtTemp)
    


# In[4]:


import re

# for converting to lower case and removing punctuation
for i in range(numberDocs):
    docs[i] = docs[i].lower()
    docs[i] = re.sub(r'[^\w\s]','',docs[i])
    


# In[5]:


dictList = [dict() for x in range(numberDocs)]

# making indiviudal dictionaries for each document
for i in range(numberDocs):
    tempDict = {}
    
    text_tokens = nltk.tokenize.word_tokenize(docs[i])
    #print(text_tokens)
    
    for j in range(len(text_tokens)):
        if(text_tokens[j] in tempDict):
            tempValue = tempDict[text_tokens[j]]
            for k in range(len(tempValue)):
                if(tempValue[k][0] == i):
                    tempValue[k][1] = tempValue[k][1] + 1
                    break
                else:
                    tempDict[text_tokens[j]].append([i,1])
        else:
            tempDict[text_tokens[j]] = [[i,1]]
    
    dictList[i] = tempDict


# In[6]:


# function to merge two dictionaries

def mergeDict(dict1, dict2):
    result = {}
    for key in dict1.keys():
        result[key] = dict1[key]
   
    for key in result.keys():
        if key in dict2.keys():
            for g in dict2[key]:
                result[key].append(g)
   
    for key in dict2.keys():
        if key not in result.keys():
            result[key] = dict2[key]
           
    return result


# In[7]:


# d is the final main index
d = {}
d = mergeDict(dictList[0],dictList[1])

#merging each dictionary one by one
for i in range(2,numberDocs):
    d = mergeDict(d,dictList[i])
    #print(i)


# In[8]:



try:
    import cPickle as pickle
except ImportError:  # python 3.x
    import pickle

    # saving the final index in a .p file

with open('dictionary.p', 'wb') as fp:
    pickle.dump(d, fp, protocol=pickle.HIGHEST_PROTOCOL)

