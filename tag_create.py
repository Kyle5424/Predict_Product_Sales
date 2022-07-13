import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.collocations import *
#from nltk.book import *
from pyvi import ViTokenizer
import string

bigram_measures = nltk.collocations.BigramAssocMeasures()

def preprocess(text):
    stopWord = []
    with open("vietnamese-stopwords.txt", encoding="utf-8") as sw:
        text1 = sw.read()
        for word in text1.split():
            stopWord.append(word)
        sw.close()

    words_raw = ViTokenizer.tokenize(text)
    words_raw = word_tokenize(words_raw)
    words = []
    for l in words_raw:
        l = l.lower()
        if l in stopWord:
            continue
        else:
            words.append(l)

    for k in words:
        if k in string.punctuation:
            words.remove(k)
        elif k in string.digits:
            words.remove(k)
        elif k in string.whitespace:
            words.remove(k)
        elif k == '\ufeff' and ',':
            words.remove(k)
        elif k == '"':
            words.remove(k)
    return words

f = open('vb2000/test-500/kinh doanh/4104.txt','r',encoding="utf-8")
test = f.read()
corpus = preprocess(test)

finder = BigramCollocationFinder.from_words(corpus)
finder.apply_freq_filter(3)
test2 = finder.nbest(bigram_measures.pmi, 5)
print(test2)