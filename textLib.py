import gensim
from pyvi import ViTokenizer,ViUtils,ViPosTagger,ViDiac,models
class Text:
    def __init__(self,str):
        self.str=str
        self.delTag()
        self.splitWord()
        self.normal()
        self.delStopword()
    def delTag(self):
        # xoa tag
        self.str=gensim.parsing.strip_tags(self.str)
        # xoa khoang trang
        self.str=gensim.parsing.preprocessing.strip_multiple_whitespaces(self.str)
        # xoa ki tu dac biet
        self.str=gensim.parsing.preprocessing.strip_non_alphanum(self.str)
        # xoa dau , .
        self.str=gensim.parsing.preprocessing.strip_punctuation(self.str)
        # xoa so
        self.str=gensim.parsing.preprocessing.strip_numeric(self.str)

    def splitWord(self):
        self.str=ViTokenizer.tokenize(self.str)
    def normal(self):
        self.str=gensim.parsing.preprocessing.stem_text(self.str)
    def delStopword(self):
        stop_word = []
        with open("stopword.txt", encoding="utf-8") as f:
            text = f.read()
            for word in text.split():
                stop_word.append(word)
            f.close()
        str=self.str.split(" ")
        self.str = ""
        for word in str:
            if word not in stop_word:
                self.str+=word+" "