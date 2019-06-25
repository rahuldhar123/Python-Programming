import requests as rq
import nltk
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import wordpunct_tokenize,pos_tag,ne_chunk

response=rq.get("https://en.wikipedia.org/wiki/Google")
cont=BeautifulSoup(response.content,"html.parser")
#print(cont.text)
text = 'Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California. Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet\'s leading subsidiary and will continue to be the umbrella company for Alphabet\'s Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet. ';
#Tokenization
print("____________Tokenization______________")
stokens = nltk.sent_tokenize(text)
wtokens = nltk.word_tokenize(text)
for s in stokens:
    print(s)
for w in wtokens:
   print(w)

#POS Tagging
print("____________POS Tagging______________")
print(nltk.pos_tag(wtokens))

#Stemming
print("____________Stemming______________")
pStemmer = PorterStemmer()
for w in wtokens:
   print(w," : ", pStemmer.stem(w))
pStemmer = LancasterStemmer()
for w in wtokens:
    print(w," : ", pStemmer.stem(w))

#Lemmatization
print("____________Lemmetization______________")
lemmetizer = WordNetLemmatizer()
for w in wtokens:
   print(w," : ", lemmetizer.lemmatize(w))

#Trigram
print("____________Trigrams______________")
new_trigrams = []
c = 0
while c < len(wtokens) - 2:
    new_trigrams.append((wtokens[c], wtokens[c+1], wtokens[c+2]))
    c += 2
for trigram in new_trigrams:
    print(trigram)

#Named Entity Recognition
print("____________Named Entity Recognition______________")
print(ne_chunk(pos_tag(wordpunct_tokenize(text))))