# coding: UTF-8
__author__ = 'mywo'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1

            # select the smaller list
            if l1.val < l2.val:
                merged_list_head = l1
                b_list_head = l2
            else:
                merged_list_head = l2
                b_list_head = l1

            merged_list_tail = merged_list_head
            a_list_head = merged_list_head.next

            while True:
                if not a_list_head:
                    merged_list_tail.next = b_list_head
                    break
                if not b_list_head:
                    merged_list_tail.next = a_list_head
                    break

                if a_list_head.val < b_list_head.val:
                    merged_list_tail.next = a_list_head
                    a_list_head = a_list_head.next
                else:
                    merged_list_tail.next = b_list_head
                    b_list_head = b_list_head.next
                merged_list_tail = merged_list_tail.next
            return merged_list_head
