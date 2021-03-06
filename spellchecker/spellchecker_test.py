# -*- coding: utf-8 -*-

import unittest

from spellchecker import SpellChecker

class TestSpellChecker(unittest.TestCase):

    # this method is executed before each test method
    def setUp(self):
        self.spellChecker = SpellChecker()
        # instead of use the function to load one file
        #    self.spellChecker.load_words('spell.words')
        # let's call the new function below to read all files in the specified folder 'dic'
        self.spellChecker.load_words_from_dir('dic/*.words')

    def test_dictionary_of_words(self):
        self.assertTrue(len(self.spellChecker.words) == 53751) 

    # when changing the function load_words for load_words_from_dir
    # all the existing tests below should work in the same way, otherwise
    # the new function is not working
    def test_spell_checker(self):
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        self.assertFalse(self.spellChecker.check_word('mistasdas'))
        self.assertTrue(
            len(self.spellChecker.check_words('zygotic mistasdas elementary')) == 1)
        self.assertTrue(len(self.spellChecker.check_words('our first correct sentence')) == 0)
        self.assertTrue(len(self.spellChecker.check_words('Our first correct sentence.')) == 0)
        failed_words = self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')
        self.assertTrue(len(failed_words) == 2)
        self.assertTrue(failed_words[0]['word'] == 'mistasdas')
        self.assertTrue(failed_words[0]['line'] == 1)
        self.assertEqual(9, failed_words[0]['pos'])
        self.assertEqual('spelling', failed_words[0]['type'])
        self.assertTrue(failed_words[1]['word'] == 'spelllleeeing')
        self.assertTrue(failed_words[1]['line'] == 1)
        self.assertTrue(failed_words[1]['pos'] == 19)
        self.assertEqual('spelling', failed_words[1]['type'])
        #self.assertEquals(0,
        #    len(self.spellChecker.check_document('spell.words')))
        failed_profane_words = self.spellChecker.check_document('profanity.txt')
        self.assertEqual(3, len(failed_profane_words))
        self.assertEqual('profanity', failed_profane_words[0]['type'])

if __name__ == '__main__':
    unittest.main()
