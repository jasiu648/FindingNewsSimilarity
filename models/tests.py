import unittest
from unittest.mock import MagicMock, patch
from collections import Counter
from Model import *
from ner_models import *

class TestEnglishNERModel(unittest.TestCase):

    def setUp(self):
        self.ner_model = spacy.load('en_core_web_trf', disable=["tagger", "parser", "attribute_ruler", "lemmatizer"])

    def test_person_recognition(self):
        
    def test_place_recognition(self):
    
    def test_org_regognition(self):

    def test_no_ner(self):
    
    def test_fake_ner(self):
    
    def test_random_ner(self):
