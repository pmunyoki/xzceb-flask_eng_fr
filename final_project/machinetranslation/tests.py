import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslationMethods(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertNotEqual(frenchToEnglish('Bonjour'),None)
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

    def test_englishToFrench(self):
        self.assertNotEqual(englishToFrench('Hello'), None)
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

if __name__ == "__main__":
    unittest.main()
    
