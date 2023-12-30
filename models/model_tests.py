import unittest
from unittest.mock import MagicMock, patch
from collections import Counter
from model import *

class TestTfIdfModel(unittest.TestCase):
    def setUp(self):
        
        self.tfidf_model = TfIdfModel()
    
    def test_nomatching_words(self):

        corpus = ["This is a sample article.", "Another document for testing TF-IDF."]
        result = self.tfidf_model.Transform(corpus)
        expected = 0

        self.assertEqual(result[0][1], expected)

    def test_sametext(self):

        corpus = ["This is a sample article.", "This is a sample article."]
        result = self.tfidf_model.Transform(corpus)
        expected = 1

        self.assertAlmostEqual(result[0][1], expected, delta = 0.00001)

    def test_attribute_input(self):
        with self.assertRaises(AttributeError):
            self.tfidf_model.Transform([1,2])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.tfidf_model.Transform([])

if __name__ == '__main__':
    unittest.main(verbosity=2)