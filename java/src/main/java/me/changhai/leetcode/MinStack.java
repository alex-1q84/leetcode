package me.changhai.leetcode;

/**
 * Created by bl02515 on 14/12/7.
 */
class MinStack {
    private Node realStackHead = null;

    private Node minStack = null;

    private int size = 0;

    public void push(int x) {
        realStackHead = new Node(x, realStackHead);
        if (minStack == null) {
            minStack = new Node(x, minStack);
        }
        else {
            int min = minStack.value > realStackHead.value ? realStackHead.value : minStack.value;
            minStack = new Node(min, minStack);
        }
        this.size += 1;
    }

    public void pop() {
        if (realStackHead != null) {
            realStackHead = realStackHead.next;
            minStack = minStack.next;
            this.size -= 1;
        }
    }

    public int top() {
        return realStackHead.value;
    }

    public int getMin() {
        if (minStack == null) {
            throw new RuntimeException("stack is empty");
        }
        return minStack.value;
    }

    public int size() {
        return this.size;
    }

    private static class Node {
        private final int value;

        private Node next;

        private Node(int value, Node next) {
            this.value = value;
            this.next = next;
        }
    }
}

