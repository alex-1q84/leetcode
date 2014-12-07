package me.changhai.leetcode;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class WordsReverseTest {

    private WordsReverse reverse;

    @Before
    public void setUp() throws Exception {
        reverse = new WordsReverse();
    }

    @Test
    public void testReverseWords() throws Exception {
        assertThat(reverse.reverseWords("the sky is blue"), is("blue is sky the"));
    }

    @Test
    public void testReverseWords_with_lead_space() throws Exception {
        assertThat(reverse.reverseWords(" 1"), is("1"));
    }

    @Test
    public void testReverseWords_with_tail_space() throws Exception {
        assertThat(reverse.reverseWords("1 "), is("1"));
    }

    @Test
    public void testReverseWords_with_multi_space() throws Exception {
        assertThat(reverse.reverseWords("1   2"), is("2 1"));
    }
}