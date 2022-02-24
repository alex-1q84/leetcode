from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def dislink_head(link: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
    head = link
    next = link.next
    head.next = None
    return head, next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 比较两个链表头的值，如果值较小则把这个节点摘下来挂到新链表末尾，并把链表头指向下一个节点
        # 直到其中一个链表头为 None，则说明这个链表已经遍历完成，则把另一个链表剩余部分挂到新链表末尾，完成合并
        new_link = None
        new_link_tail = new_link
        h1, h2 = list1, list2
        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                if new_link is None:
                    new_link, h1 = dislink_head(h1)
                    new_link_tail = new_link
                else:
                    new_link_tail.next, h1 = dislink_head(h1)
                    new_link_tail = new_link_tail.next
            else:
                if new_link is None:
                    new_link, h2 = dislink_head(h2)
                    new_link_tail = new_link
                else:
                    new_link_tail.next, h2 = dislink_head(h2)
                    new_link_tail = new_link_tail.next

        if h1 != None:
            if new_link is None:
                new_link = h1
            else:
                new_link_tail.next = h1
        else:
            if new_link is None:
                new_link = h2
            else:
                new_link_tail.next = h2

        return new_link
