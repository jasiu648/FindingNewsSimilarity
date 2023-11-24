from abc import ABC, abstractmethod
import spacy
import spacy_transformers

class NER(ABC):

    @abstractmethod
    def __init__(self):
        self.language = 'None'

    @abstractmethod
    def FindNamedEntites():
        pass
    
class PolishNER(NER):

    def __init__(self):
        self.ner_model = spacy.load('pl_core_news_lg')
        self.language = 'PL'
        
    def FindNamedEntites(self, text):
        entities = self.ner_model(text)
        named_entities = [(ent.text, ent.label_) for ent in entities.ents ]
        print(named_entities)

class SlovenianNER(NER):

    def __init__(self):
        self.ner_model = spacy.load('sl_core_news_trf')
        self.language = 'SL'
        
    def FindNamedEntites(self, text):
        entities = self.ner_model(text)
        named_entities = [(ent.text, ent.label_) for ent in entities.ents ]
        print(named_entities)

class EnglishNER(NER):

    def __init__(self):
        self.ner_model = spacy.load('en_core_news_trf')
        self.language = 'EN'
        
    def FindNamedEntites(self, text):
        entities = self.ner_model(text)
        named_entities = [(ent.text, ent.label_) for ent in entities.ents ]
        print(named_entities)

class CroatianNER(NER):

    def __init__(self):
        self.ner_model = spacy.load('hr_core_news_lg')
        self.language = 'HR'
        
    def FindNamedEntites(self, text):
        entities = self.ner_model(text)
        named_entities = [(ent.text, ent.label_) for ent in entities.ents ]
        print(named_entities)