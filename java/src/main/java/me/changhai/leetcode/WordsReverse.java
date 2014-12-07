package me.changhai.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by bl02515 on 14/11/10.
 */
public class WordsReverse {
    public String reverseWords(String s) {
        if (s == null) {
            return s;
        }

        String[] words = s.trim().split(" +");
        StringBuilder reversedWords = new StringBuilder(s.length());
        for (int i = words.length - 1; i >= 0 ; i--) {
            reversedWords.append(words[i]);
            if (i > 0) {
                reversedWords.append(" ");
            }
        }
        return reversedWords.toString();
    }
}
