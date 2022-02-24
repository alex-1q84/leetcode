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
    def mergeTwoLists_recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 递归
        # 找出当前两个链表头中较小的一个，则合并后的链表为这个较小的链表头加上该链表剩余节点与另一个链表的合并链表
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_recursive(list1, list2.next)
            return list2


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 比较两个链表头的值，如果值较小则把这个节点摘下来挂到新链表末尾，并把链表头指向下一个节点
        # 直到其中一个链表头为 None，则说明这个链表已经遍历完成，则把另一个链表剩余部分挂到新链表末尾，完成合并

        # 用一个假链头来解决空链表初始化问题
        dummy_head = ListNode(0)
        new_link_tail = dummy_head
        h1, h2 = list1, list2
        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                new_link_tail.next, h1 = dislink_head(h1)
                new_link_tail = new_link_tail.next
            else:
                new_link_tail.next, h2 = dislink_head(h2)
                new_link_tail = new_link_tail.next

        if h1 is not None:
            new_link_tail.next = h1
        else:
            new_link_tail.next = h2

        return dummy_head.next
