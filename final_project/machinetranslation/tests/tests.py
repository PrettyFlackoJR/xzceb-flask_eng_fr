import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslation(unittest.TestCase):
    def testF2E(self):
        self.assertEqual(frenchToEnglish('Bonjour')['translations'][0]['translation'], 
        'Hello')
        self.assertRaises(ValueError, frenchToEnglish, None)

    def testE2F(self):
        self.assertEqual(englishToFrench('Hello')['translations'][0]['translation'], 
        'Bonjour')
        self.assertRaises(ValueError, englishToFrench, None)
        
unittest.main()