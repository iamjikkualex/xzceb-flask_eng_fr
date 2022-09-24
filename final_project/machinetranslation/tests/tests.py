import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_for_null(self):
        self.assertEqual(english_to_french(" "), " ")

    def test_for_translation1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_for_translation2(self):
        self.assertNotEqual(english_to_french('Hello'), 'Bonne nuit')

class TestFrenchToEnglish(unittest.TestCase):
    def test_for_null(self):
        self.assertEqual(french_to_english(" "), " ")

    def test_for_translation1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_for_translation2(self):
        self.assertNotEqual(french_to_english('Bonne nuit'), 'Hello')

unittest.main()

