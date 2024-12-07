from pyvi import ViTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics
import pickle
import numpy as np
class classification:
    def __init__(self):
        self.X_data = pickle.load(open('X_train1.pkl', 'rb'))
        self.y_data = pickle.load(open('y_train1.pkl', 'rb'))
        self.X_test = pickle.load(open('X_test1.pkl', 'rb'))
        self.y_test = pickle.load(open('y_test1.pkl', 'rb'))
        print(len(self.X_data))
        print(len(self.X_test))
        self.model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        self.model.fit(self.X_data, self.y_data)
        # predicted_categories = model.predict(X_test)

    def sk_predictions(self, my_sentence):
        import textLib
        my_sentence = textLib.Text(my_sentence).str
        my_sentence = ViTokenizer.tokenize(my_sentence)
        prediction = self.model.predict([my_sentence])
        return prediction
    def my_predictions(self,my_sentence):
        tf_vectorizer = CountVectorizer()
        X_data_tf = tf_vectorizer.fit_transform(self.X_data)
        naive_bayes_classifier = MultinomialNB()
        naive_bayes_classifier.fit(X_data_tf, self.y_data)
        prediction = naive_bayes_classifier.predict(tf_vectorizer.transform([my_sentence]))
        return prediction
    def getScore(self):
        prediction_score = self.model.predict(self.X_test)
        print("Percent = ",np.mean(prediction_score==self.y_test))
# a = classification()
# a.getScore()
