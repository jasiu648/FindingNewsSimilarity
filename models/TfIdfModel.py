from Model import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TfIdfModel(Model):
    
    def Transform(self, corpus, ngram_lower_bound = 2, ngram_upper_bound = 4):
        tfidf = TfidfVectorizer(ngram_range=(2,4), max_df=0.25)

        tfidf_matrix = tfidf.fit_transform(corpus)

        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        return cosine_sim