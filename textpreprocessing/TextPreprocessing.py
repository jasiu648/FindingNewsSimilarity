from abc import ABC, abstractmethod
import spacy
import string
from collections import Counter
from nltk.tokenize import word_tokenize
class TextPreprocessor:
    
    def __init__(self):
        self.language_model = None
        self.stopwords = None

    def preprocess_text(self, text, apply_lemmatization = False, apply_stemming = False):
    
        tokens = word_tokenize(text)
        tokens = [word.lower() for word in tokens]

        tokens = [word for word in tokens if word.isalnum()]

        tokens = self.remove_stopwords(tokens)

        if apply_lemmatization:
            
            doc = self.language_model(' '.join(tokens))
            tokens = [token.lemma_ for token in doc if token.text not in string.punctuation]
        
        #if apply_stemming:
        #    stemmer = PorterStemmer()
        #    tokens = [stemmer.stem(word) for word in tokens]

        return tokens
    
    def convert_to_BoW(self, text):

        tokens = self.preprocess_text(text)
        word_counts = Counter(tokens)
        return word_counts
    
    def create_set_from_file(self, file_path):
        
        string_set = set()

        with open(file_path, 'r') as file:
            string_set.update(line.strip() for line in file)

        return string_set
    
    def remove_stopwords(self, tokens):

        tokens_without_stopwords = [word for word in tokens if word not in self.stopwords ]

        return tokens_without_stopwords
        
    

class PolishTextPreprocessor(TextPreprocessor):

    def __init__(self):
        self.language_model = spacy.load('pl_core_news_lg')
        self.stopwords = self.create_set_from_file('stopwords/polish_stopwords.txt')

class EnglishTextPreprocessor(TextPreprocessor):

    def __init__(self):
        self.language_model = spacy.load('en_core_news_trf')
        self.stopwords = self.create_set_from_file('stopwords/english_stopwords.txt')

class CroatianTextPreprocessor(TextPreprocessor):

    def __init__(self):
        self.language_model = spacy.load('hr_core_news_lg')
        self.stopwords = self.create_set_from_file('stopwords/croatian_stopwords.txt')

class SlovenianTextPreprocessor(TextPreprocessor):

    def __init__(self):
        self.language_model = spacy.load('sl_core_news_trf')
        self.stopwords = self.create_set_from_file('stopwords/slovenian_stopwords.txt')
