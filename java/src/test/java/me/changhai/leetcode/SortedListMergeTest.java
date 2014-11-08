package me.changhai.leetcode;

import static me.changhai.leetcode.SortedListMerge.ListNode;
import static org.junit.Assert.*;

import java.util.Arrays;

import org.junit.Before;
import org.junit.Test;

public class SortedListMergeTest {

    private SortedListMerge sortedListMerge;

    @Before
    public void setUp() throws Exception {
        sortedListMerge = new SortedListMerge();
    }

    @Test
    public void testMergeTwoLists() throws Exception {
        assertMergesEquals(new int[] { 1, 2, 4, 5 }, new int[] { 5 }, new int[] { 1, 2, 4 });
    }

    @Test
    public void testMergeTwoLists_1() throws Exception {
        assertMergesEquals(new int[] { 1, 2, 4, 5 }, new int[] { 1, 2, 4 }, new int[] { 5 });
    }

    @Test
    public void testMergeTwoLists_2() throws Exception {
        assertMergesEquals(new int[] { 1, 2, 3, 4, 5 }, new int[] { 1, 2, 4 }, new int[] { 3, 5 });
    }

    void assertMergesEquals(int[] expect, int[] nodes1, int[] nodes2) {
        ListNode l1 = createNodeList(nodes1);
        ListNode l2 = createNodeList(nodes2);
        ListNode merged = sortedListMerge.mergeTwoLists(l1, l2);
        assertEquals(Arrays.toString(expect), toString(merged));
    }

    ListNode createNodeList(int[] ints) {
        if (ints == null || ints.length == 0) {
            throw new IllegalArgumentException("列表不能为空");
        }

        if (ints.length == 1) {
            return new ListNode(ints[0]);
        }

        ListNode head, tail;
        head = tail = new ListNode(ints[0]);
        for (int i = 1; i < ints.length; i++) {
            tail.next = new ListNode(ints[i]);
            tail = tail.next;
        }
        return head;
    }

    String toString(ListNode node) {
        StringBuilder result = new StringBuilder("[");
        while (node != null) {
            result.append(node.val);
            node = node.next;
            if (node != null) {
                result.append(", ");
            }
        }
        result.append("]");
        return result.toString();
    }
}