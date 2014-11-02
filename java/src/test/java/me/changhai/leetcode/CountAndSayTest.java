package me.changhai.leetcode;

import static org.junit.Assert.*;

import org.junit.Test;

public class CountAndSayTest {

    @Test
    public void testCountAndSay_1() {
        CountAndSay countAndSay = new CountAndSay();
        assertEquals("1", countAndSay.countAndSay(1));
    }

    @Test
    public void testCountAndSay_2() {
        CountAndSay countAndSay = new CountAndSay();
        assertEquals("11", countAndSay.countAndSay(2));
    }

    @Test
    public void testCountAndSay_3() {
        CountAndSay countAndSay = new CountAndSay();
        assertEquals("21", countAndSay.countAndSay(3));
    }

    @Test
    public void testCountAndSay_4() {
        CountAndSay countAndSay = new CountAndSay();
        assertEquals("1211", countAndSay.countAndSay(4));
    }

    @Test
    public void testCountAndSay_5() {
        CountAndSay countAndSay = new CountAndSay();
        assertEquals("111221", countAndSay.countAndSay(5));
    }

    @Test
    public void testDescNumber() {
        CountAndSay countAndSay = new CountAndSay();
        assertEquals("1211", countAndSay.descNumber("21"));
    }
}