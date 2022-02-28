# 202202281424
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 快慢指针，快指针先走 n-1 步，然后快慢指针同步走，都快指针走到末尾，删除慢指针当前位置节点并返回
        dummy_head = ListNode()
        new_link_tail = dummy_head
        slow, fast = head, head
        i = 0
        while fast.next and i < n - 1:
            fast = fast.next
            i += 1

        while fast.next:
            fast = fast.next
            new_link_tail.next = slow
            new_link_tail = new_link_tail.next
            slow = slow.next
        new_link_tail.next = slow.next
        return dummy_head.next
