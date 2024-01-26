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
    
    def Transform2(self, corpus):
        # Encode the entire corpus into embeddings
        embeddings = self.model.encode(corpus, convert_to_tensor=True)

        # Calculate cosine similarity between all pairs of embeddings
        similarity_matrix = util.pytorch_cos_sim(embeddings, embeddings)

        # Convert the similarity matrix to a NumPy array
        similarity_matrix_np = similarity_matrix.cpu().numpy()

        return similarity_matrix_np
    
class PolishBertModel(BertModel):

    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

class EnglishBertModel(BertModel):

    def __init__(self):
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

class SlovenianBertModel(BertModel):

    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

class CroatianBertModel(BertModel):

    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

class TfIdfModel(Model):
    
    def Transform(self, corpus, ngram_lower_bound = 2, ngram_upper_bound = 4):
        tfidf = TfidfVectorizer(ngram_range=(ngram_lower_bound,ngram_upper_bound))

        tfidf_matrix = tfidf.fit_transform(corpus)

        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        return cosine_sim