import unittest
from models.model import *
from models.ner_models import *
from textpreprocessing.TextPreprocessing import *
from data_access.DataProvider import *
class TestIntegrationModules(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_check_types(self):
        
        model = TfIdfModel()
        pl_model = PolishBertModel()
        en_model = EnglishBertModel()

        self.assertIsInstance(model, Model)
        self.assertNotIsInstance(model, BertModel)

        self.assertIsInstance(model,TfIdfModel)
        self.assertIsInstance(pl_model, Model)
        self.assertIsInstance(en_model, Model)


    def test_polish_pipeline(self):
        text1 = "Tekst dla sprawdzanie polskiego pipeline"
        text2 = "Drugi tekst dla sprawdzenia poprawnosci polskiej"
        pl_model = PolishBertModel()
        pl_preprocess = PolishTextPreprocessor()
        pl_tfidf = TfIdfModel()
        
        res_bert = pl_model.Transform(text1, text2)
        text1 = pl_preprocess.preprocess_text(text1,True)
        text2 = pl_preprocess.preprocess_text(text2,True)
        res_tf = pl_tfidf.Transform([text1, text2])

        self.assertAlmostEqual(res_bert , 0.93, delta = 0.01)
        self.assertAlmostEqual(res_tf[0][1], 0, delta = 0.01)


    def test_english_pipeline(self):
        text1 = "Text to chech english pipeline"
        text2 = "Second text to check if english is ok"
        en_model = EnglishBertModel()
        en_preprocess = EnglishTextPreprocessor()
        en_tfidf = TfIdfModel()
        
        res_bert = en_model.Transform(text1, text2)
        text1 = en_preprocess.preprocess_text(text1)
        text2 = en_preprocess.preprocess_text(text2)
        res_tf = en_tfidf.Transform([text1, text2])

        self.assertAlmostEqual(res_bert , 0.40, delta = 0.01)
        self.assertAlmostEqual(res_tf[0][1], 0, delta = 0.01)

if __name__ == '__main__':
    unittest.main(verbosity=2)