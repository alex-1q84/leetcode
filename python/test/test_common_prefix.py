from unittest import TestCase
from leetcode.common_prefix import Solution

__author__ = 'mywo'


class TestSolution(TestCase):
    def test_empty_list(self):
        solution = Solution()
        prefix = solution.longestCommonPrefix([])
        self.assertEqual('', prefix, 'prefix should be empty')

    def test_one_item_list(self):
        solution = Solution()
        prefix = solution.longestCommonPrefix(['abc'])
        self.assertEqual('abc', prefix, 'longest common prefix should be abc')

    def test_single_char_items(self):
        solution = Solution()
        prefix = solution.longestCommonPrefix(['c', 'c'])
        self.assertEqual('c', prefix, 'longest common prefix should be c')

    def test_multi_item_list(self):
        solution = Solution()
        prefix = solution.longestCommonPrefix(['abc', 'abd'])
        self.assertEqual('ab', prefix, 'longest common prefix should be ab')

    def test_multi_same_item_list(self):
        solution = Solution()
        prefix = solution.longestCommonPrefix(['abc', 'abc'])
        self.assertEqual('abc', prefix, 'longest common prefix should be abc')