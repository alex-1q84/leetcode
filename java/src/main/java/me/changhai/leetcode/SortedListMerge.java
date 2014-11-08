package me.changhai.leetcode;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class SortedListMerge {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        if (l2 == null) {
            return l1;
        }

        ListNode mergedListHead = null;
        ListNode bListHead = null;
        if (l1.val < l2.val) {
            mergedListHead = l1;
            bListHead = l2;
        }
        else{
            mergedListHead = l2;
            bListHead = l1;
        }
        ListNode mergedListTail = mergedListHead;
        ListNode aListHead = mergedListHead.next;
        mergedListTail.next = null;

        while(true) {
            if (aListHead == null) {
                mergedListTail.next = bListHead;
                break;
            }

            if (bListHead == null) {
                mergedListTail.next = aListHead;
                break;
            }

            if (bListHead.val < aListHead.val) {
                mergedListTail.next = bListHead;
                bListHead = bListHead.next;
            }else{
                mergedListTail.next = aListHead;
                aListHead = aListHead.next;
            }
            mergedListTail = mergedListTail.next;
        }

        return mergedListHead;
    }

    public static class ListNode {
        int val;

        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }

        @Override
        public String toString() {
            return String.format("(%s -> %s)", val, next == null ? null : next.val);
        }
    }
}
