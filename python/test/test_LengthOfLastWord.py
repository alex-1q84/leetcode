from unittest import TestCase

__author__ = 'mywo'

from leetcode.LengthOfLastWord import Soulution

class TestSoulution(TestCase):

    def setUp(self):
        super(TestSoulution, self).setUp()
        self.soulution = Soulution()


    def test_lengthOfLastWord_blank(self):
        self.assertEqual(0, self.soulution.lengthOfLastWord(""))


    def test_lengthOfLastWord_space_worl(self):
        self.assertEqual(0, self.soulution.lengthOfLastWord(" "))


    def test_lengthOfLastWord_one_word(self):
        self.assertEqual(1, self.soulution.lengthOfLastWord("a"))


    def test_lengthOfLastWord_multi_words(self):
        self.assertEqual(2, self.soulution.lengthOfLastWord("a bc"))
