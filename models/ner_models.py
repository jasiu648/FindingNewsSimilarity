from abc import ABC, abstractmethod
import spacy
import spacy_transformers

class NER(ABC):

    @abstractmethod
    def __init__(self):
        self.ner_model = None
        self.language = 'None'

    def FindNamedEntites(self, text):
        entities = self.ner_model(text)
        named_entities = [(ent.text, ent.label_) for ent in entities.ents ]
        return named_entities
    
class PolishNER(NER):

    def __init__(self):
        self.ner_model = spacy.load('pl_core_news_lg')
        self.language = 'PL'
        

class SlovenianNER(NER):

    def __init__(self):
        self.ner_model = spacy.load('sl_core_news_trf')
        self.language = 'SL'
    

class EnglishNER(NER):

    def __init__(self):
        self.ner_model = spacy.load('en_core_web_trf', disable=["tagger", "parser", "attribute_ruler", "lemmatizer"])
        self.language = 'EN'

class CroatianNER(NER):

    def __init__(self):
        self.ner_model = spacy.load('hr_core_news_lg', disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"])
        self.language = 'HR'
        