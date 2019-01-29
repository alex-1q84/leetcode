from unittest import TestCase

__author__ = 'mywo'

from leetcode.SortedListMerge import *


class TestSolution(TestCase):
    def test_mergeTwoLists_with_one_list_empty(self):
        l1 = ListNode(1)
        l2 = None
        solution = Solution()
        self.assertEqual(l1, solution.mergeTwoLists(l1, l2))

    def test_mergeTwoLists(self):
        l1 = ListNode(1)

        l2 = None
        solution = Solution()
        self.assertEqual(l1, solution.mergeTwoLists(l1, l2))

def _make_list(*vals):
    if not vals:
        return None

    for val in (ListNode(i) for i in vals):
        pass
