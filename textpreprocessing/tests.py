import unittest
from unittest.mock import MagicMock, patch
from collections import Counter
from TextPreprocessing import *

class TestEnglishTextPreprocessor(unittest.TestCase):

    def setUp(self):
        # Set up any necessary objects or configurations for testing
        self.text_preprocessor = EnglishTextPreprocessor()

    def test_remove_stopwords(self):
        text = "this a now just what where to as where when"
        result = self.text_preprocessor.preprocess_text(text)
        expected = []
        self.assertEqual(result,expected)

    def test_preprocess_text_no_lemmatization_no_stemming(self):
        text = "This is a simple test."

        result = self.text_preprocessor.preprocess_text(text)

        expected = ['simple', 'test']
        self.assertEqual(result, expected)

    def test_preprocess_text_with_lemmatization(self):
        text = "The cats are running and jumping over fences."

        result = self.text_preprocessor.preprocess_text(text, apply_lemmatization=True)

        expected = ['cat', 'run', 'jump', 'fence']
        self.assertEqual(result, expected)

class TestPolishTextPreprocessor(unittest.TestCase):

    def setUp(self):
        # Set up any necessary objects or configurations for testing
        self.text_preprocessor = PolishTextPreprocessor()

    def test_remove_stopwords(self):
        text = "Teraz jak aby ale co gdzie wy ja ty"
        result = self.text_preprocessor.preprocess_text(text)
        expected = []
        self.assertEqual(result,expected)

    def test_preprocess_text_no_lemmatization_no_stemming(self):
        text = "To jest prosty test systemu"

        result = self.text_preprocessor.preprocess_text(text)

        expected = ['prosty','test','systemu']
        self.assertEqual(result, expected)

    def test_preprocess_text_with_lemmatization(self):
        text = "Psy biegną po parku i szczekają na ptaki."

        result = self.text_preprocessor.preprocess_text(text, apply_lemmatization=True)

        expected = ['pies', 'biec', 'park', 'szczekać', 'ptak']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()