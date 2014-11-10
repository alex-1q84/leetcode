from unittest import TestCase
from leetcode.WordsReverse import *

__author__ = 'mywo'


class TestSolution(TestCase):
    def test_reverseWords(self):
        solution = Solution()
        self.assertEqual("blue is sky the", solution.reverseWords("the sky is blue"))
