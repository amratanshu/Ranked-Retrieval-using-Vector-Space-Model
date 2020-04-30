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

ag40 = open('wiki_40', encoding="utf8")

soup = BeautifulSoup(ag40, 'lxml')

docList = soup.findAll('doc')
numberDocs = len(docList)
docs = []

for i in range(numberDocs):
    soupTemp = BeautifulSoup(str(docList[i]))
    txtTemp = soupTemp.get_text()
    docs.append(txtTemp)
    
import re

for i in range(numberDocs):
    docs[i] = docs[i].lower()
    docs[i] = re.sub(r'[^\w\s]','',docs[i])


val = input("Enter the docID of the document you want to print - ")
print('\n\n Here is the required Document -\n')
print(docs[int(val)])   