from models.model import *
from textpreprocessing.TextPreprocessing import *
from models.ner_models import *
from utils.utils import count_jaccard_similarity

class Pipeline():
    
    def __init__(self):
        self.embedding_model = Model()
        self.preprocessing = TextPreprocessor()
        self.ner_model = NER()

    
    def ProcessPipeline(self, corpus ,Nmin, Nmax, apply_preprocessing = True):
    
        results = [ResultsDataFrame() for i in range(len(corpus))]
        tfidf_model = TfIdfModel()

        for i in range(len(corpus)):
            
            #Embedding result
            bert_res = self.embedding_model.Transform(corpus[i][0],corpus[i][1])
            
            if(bert_res < 0):
                bert_res = 0
            if(bert_res > 1):
                bert_res = 1

            results[i].embedding_result = bert_res

            #Ner result

            a1 = self.ner_model.FindNamedEntites(corpus[i][0])
            results[i].ner_1 = [inner_list[0] for inner_list in a1[i]]
            a2 = self.ner_model.FindNamedEntites(corpus[i][1])
            results[i].ner_2 = [inner_list[0] for inner_list in a2[i]]
            results[i].ner_result = count_jaccard_similarity(results[i].ner_1, results[i].ner_2)

            #Tfidf

            if(apply_preprocessing):
                corpus[i][0] = self.preprocessing.preprocess_text(corpus[i][0], apply_lemmatization= True)
                corpus[i][0] = ''.join(corpus[i][0])
                corpus[i][1] = self.preprocessing.preprocess_text(corpus[i][1], apply_lemmatization= True)
                corpus[i][1] = ''.join(corpus[i][1])

            tfidf_matrix = tfidf_model.Transform(corpus[i], Nmin, Nmax)
            results[i].tfidf_result = tfidf_matrix[0][1]
        
        return results
            

class PolishPipeline(Pipeline):

    def __init__(self):
        self.embedding_model = PolishBertModel()
        self.preprocessing = PolishTextPreprocessor()
        self.ner_model = PolishNER()

class EnglishPipeline(Pipeline):

    def __init__(self):
        self.embedding_model = EnglishBertModel()
        self.preprocessing = EnglishTextPreprocessor()
        self.ner_model = EnglishNER()

class SlovenianPipeline(Pipeline):

    def __init__(self):
        self.embedding_model = EnglishBertModel()
        self.preprocessing = SlovenianTextPreprocessor()
        self.ner_model = SlovenianNER()

class CroatianPipeline(Pipeline):

    def __init__(self):
        self.embedding_model = EnglishBertModel()
        self.preprocessing = CroatianTextPreprocessor()
        self.ner_model = CroatianNER()

class ResultsDataFrame():

    def __init__(self, embedding_result = None, tfidf_result = None, ner_result = None):
        self.embedding_result = embedding_result
        self.tfidf_result = tfidf_result
        self.ner_result = ner_result
        self.ner1 = None
        self.ner2 = None
        

    def print_results(self):
        print(f"Embedding Result: {self.embedding_result}")
        print(f"TF-IDF Result: {self.tfidf_result}")
        print(f"NER Result: {self.ner_result}")

class PipelineFactory():

    def __init__(self):
        pass
    
    @staticmethod
    def CreatePipeline(language = 'PL'):
        pipe = None
        if language == 'PL':
            pipe = PolishPipeline()      
        elif language == 'EN':
            pipe = EnglishPipeline()  
        elif language == 'SL':
            pipe = SlovenianPipeline()  
        elif language == 'HR':
            pipe = CroatianPipeline()  
        else:
            print('Invalid option')

        return pipe
