import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_for_null(self):
        self.assertEqual(english_to_french(" "), " ")

    def test_for_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test_for_null(self):
        self.assertEqual(french_to_english(" "), " ")

    def test_for_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()

