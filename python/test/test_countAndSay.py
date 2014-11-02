from unittest import TestCase

__author__ = 'mywo'

from leetcode.CountAndSay import *


class TestSoulution(TestCase):
    def test_countAndSay_1(self):
        solution = Solution()
        self.assertEqual("1", solution.countAndSay(1))


    def test_countAndSay_12(self):
        solution = Solution()
        self.assertEqual("11", solution.countAndSay(2))


    def test_countAndSay_1_11(self):
        solution = Solution()
        self.assertEqual("21", solution.countAndSay(3))


    def test_countAndSay_1_11_21(self):
        solution = Solution()
        self.assertEqual("1211", solution.countAndSay(4))


    def test_countAndSay_1_11_2222_3(self):
        solution = Solution()
        self.assertEqual("111221", solution.countAndSay(5))

