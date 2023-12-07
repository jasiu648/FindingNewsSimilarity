from abc import ABC, abstractmethod

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

class Model(ABC):

    @abstractmethod
    def Transform():
        pass

class BertModel(Model):
    
    def __init__(self):
        self.model = None

    def Transform(self,text1, text2):
        
        embeddings = self.model.encode([text1, text2], convert_to_tensor=True)

        # Calculate cosine similarity between the embeddings
        similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1])

        return similarity_score.item()
    
class PolishBertModel(BertModel):

    def __init__(self):
        self.model = SentenceTransformer("sdadas/mmlw-roberta-large")

class EnglishBertModel(BertModel):

    def __init__(self):
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    
class TfIdfModel(Model):
    
    def Transform(self, corpus, ngram_lower_bound = 2, ngram_upper_bound = 4):
        tfidf = TfidfVectorizer(ngram_range=(2,4))

        
        tfidf_matrix = tfidf.fit_transform(corpus)

        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

        return cosine_sim