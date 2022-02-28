# 202202280915
# https://leetcode-cn.com/problems/middle-of-the-linked-list/
# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
# 如果有两个中间结点，则返回第二个中间结点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 快慢指针，快指针走两步，慢指针走一步，直到快指针当前节点为空
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
