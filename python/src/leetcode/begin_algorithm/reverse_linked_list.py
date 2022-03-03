# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 1. 把当前节点设置为新链表的头
        # 2. 取出节点的下一个节点
        # 3. 如此往复，直到当前节点为 None
        new_link = None
        current = head
        while current != None:
            n = current.next
            current.next = new_link
            new_link = current
            current = n
        return new_link


