import unittest
from unittest.mock import MagicMock, patch
from collections import Counter

from ner_models import *

class TestEnglishNERModel(unittest.TestCase):

    def setUp(self):
        self.ner_model = EnglishNER()

    def test_person_recognition(self):
        text = "Barack Obama in White House meets Eminem"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Barack Obama', 'White House', 'Eminem']
        self.assertEqual(result,expected)

    def test_place_recognition(self):

        text = "Empire State Building is higher than Eiffel Tower"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Empire State Building', 'Eiffel Tower']
        self.assertEqual(result,expected)

    def test_org_regognition(self):

        text = "Google co-operates with Amazon on Apple projects"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Google', 'Amazon', 'Apple']
        self.assertEqual(result,expected)

    def test_no_ner(self):

        text = "Money does not give happiness"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = []
        self.assertEqual(result,expected)

class TestPolishNERModel(unittest.TestCase):

    def setUp(self):
        self.ner_model = PolishNER()

    def test_person_recognition(self):
        text = "Andrzej Duda w Pałacu Prezydenckim wita się z Dodą"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Andrzej Duda', 'Pałacu Prezydenckim', 'Dodą']
        self.assertEqual(result,expected)

    def test_place_recognition(self):

        text = "Pałac Kultury i Nauki jest wyższy niż Muzeum Narodowe"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Pałac Kultury i Nauki','Muzeum Narodowe']
        self.assertEqual(result,expected)

    def test_org_regognition(self):

        text = "PZPN współpracuje z Legią Warszawa"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['PZPN', 'Legią Warszawa']
        self.assertEqual(result,expected)

    def test_no_ner(self):

        text = "Pieniądze szczęścia nie dają"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = []
        self.assertEqual(result,expected)

class TestSlovenianNERModel(unittest.TestCase):

    def setUp(self):
        self.ner_model = SlovenianNER()

    def test_person_recognition(self):
        text = "Franci Kek je priznani slovenski pisatelj"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Franci Kek']
        self.assertEqual(result,expected)

    def test_place_recognition(self):

        text = "Bled je priljubljeno turistično mesto ob Blejskem jezeru v Sloveniji"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Bled', 'Blejskem jezeru', 'Sloveniji']
        self.assertEqual(result,expected)

    def test_org_regognition(self):

        text = "Univerza v Ljubljani je ena najstarejših in največjih univerz v Evropi"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Univerza v Ljubljani', 'Evropi']
        self.assertEqual(result,expected)

    def test_no_ner(self):

        text = "denar ne prinaša sreče"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = []
        self.assertEqual(result,expected)


class TestCroatianNERModel(unittest.TestCase):

    def setUp(self):
        self.ner_model = CroatianNER()

    def test_person_recognition(self):
        text = "Kolinda Grabar-Kitarović bila je predsjednica Hrvatske."
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Kolinda Grabar-Kitarović', 'Hrvatske']
        self.assertEqual(result,expected)

    def test_place_recognition(self):

        text = "Nacionalni park Plitvička jezera jedno je od najljepših prirodnih čuda Hrvatske."
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Nacionalni park Plitvička', 'Hrvatske']
        self.assertEqual(result,expected)

    def test_org_regognition(self):

        text = "Hrvatska elektroprivreda (HEP) osigurava električnu energiju za cijelu zemlju."
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = ['Hrvatska elektroprivreda', 'HEP']
        self.assertEqual(result,expected)

    def test_no_ner(self):

        text = "novac ne donosi sreću"
        result_ner = self.ner_model.FindNamedEntites(text)
        result = [row[0] for row in result_ner]

        expected = []
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)