package me.changhai.leetcode;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class MinStackTest {
    private MinStack stack;

    @Before
    public void setUp() throws Exception {
        stack = new MinStack();
    }

    @Test
    public void testPush() throws Exception {
        stack.push(1);
        assertThat(stack.size(), is(1));
    }

    @Test
    public void testPop() throws Exception {
        stack.push(1);
        stack.push(2);
        stack.pop();
        assertThat(stack.top(), is(1));
        stack.pop();
        assertThat(stack.size(), is(0));
    }

    @Test
    public void testTop() throws Exception {
        stack.push(1);
        assertThat(stack.top(), is(1));
        stack.push(2);
        assertThat(stack.top(), is(2));
    }

    @Test
    public void testGetMin() throws Exception {
        stack.push(2);
        stack.push(0);
        stack.push(3);
        stack.push(0);
        assertThat(stack.getMin(), is(0));
        stack.pop();
        assertThat(stack.getMin(), is(0));
        stack.pop();
        assertThat(stack.getMin(), is(0));
        stack.pop();
        assertThat(stack.getMin(), is(2));
    }
}