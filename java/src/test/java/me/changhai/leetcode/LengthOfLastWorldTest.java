package me.changhai.leetcode;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class LengthOfLastWorldTest {

    private LengthOfLastWorld soulution;

    @Before
    public void setUp(){
        soulution = new LengthOfLastWorld();
    }

    @Test
    public void testLengthOfLastWord_just_one_word() throws Exception {
        assertEquals(1, soulution.lengthOfLastWord("a"));
    }

    @Test
    public void testLengthOfLastWord_empty() throws Exception {
        assertEquals(0, soulution.lengthOfLastWord(""));
    }

    @Test
    public void testLengthOfLastWord_space_world() throws Exception {
        assertEquals(0, soulution.lengthOfLastWord(" "));
    }

    @Test
    public void testLengthOfLastWord_multi_word() throws Exception {
        assertEquals(2, soulution.lengthOfLastWord("a bc"));
    }
}