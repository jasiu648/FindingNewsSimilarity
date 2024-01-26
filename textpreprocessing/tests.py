import unittest
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

class TestSlovenianTextPreprocessor(unittest.TestCase):

    def setUp(self):
        # Set up any necessary objects or configurations for testing
        self.text_preprocessor = SlovenianTextPreprocessor()

    def test_remove_stopwords(self):
        text = "bo cel dobra ene ga ker lepa leto"
        result = self.text_preprocessor.preprocess_text(text)
        expected = []
        self.assertEqual(result,expected)

    def test_preprocess_text_no_lemmatization_no_stemming(self):
        text = "To je preprost sistemski test"

        result = self.text_preprocessor.preprocess_text(text)

        expected = ['preprost', 'sistemski', 'test']
        self.assertEqual(result, expected)

    def test_preprocess_text_with_lemmatization(self):
        text = "Psi tekajo po parku in lajajo na ptice."

        result = self.text_preprocessor.preprocess_text(text, apply_lemmatization=True)

        expected = ['pes', 'tekati', 'park', 'lajati', 'ptica']
        self.assertEqual(result, expected)

class TestCroatianTextPreprocessor(unittest.TestCase):

    def setUp(self):
        # Set up any necessary objects or configurations for testing
        self.text_preprocessor = CroatianTextPreprocessor()

    def test_remove_stopwords(self):
        text = "bismo biste biti njemu njezin o s si"
        result = self.text_preprocessor.preprocess_text(text)
        expected = []
        self.assertEqual(result,expected)

    def test_preprocess_text_no_lemmatization_no_stemming(self):
        text = "Ovo je jednostavan test sustava"

        result = self.text_preprocessor.preprocess_text(text)

        expected = ['ovo', 'jednostavan', 'test', 'sustava']
        self.assertEqual(result, expected)

    def test_preprocess_text_with_lemmatization(self):
        text = "Psi trče po parku i laju na ptice."

        result = self.text_preprocessor.preprocess_text(text, apply_lemmatization=True)

        expected = ['pas', 'trčiti', 'park', 'lati', 'ptica']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)