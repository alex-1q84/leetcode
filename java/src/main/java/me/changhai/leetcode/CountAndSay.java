package me.changhai.leetcode;

/**
 * The count-and-say sequence is the sequence of integers beginning as follows:
 * 1, 11, 21, 1211, 111221, ...
 * <p/>
 * 1 is read off as "one 1" or 11.
 * 11 is read off as "two 1s" or 21.
 * 21 is read off as "one 2, then one 1" or 1211.
 * Given an integer n, generate the nth sequence.
 * <p/>
 * Note: The sequence of integers will be represented as a string.
 * <p/>
 * Created by bl02515 on 14/11/2.
 */
public class CountAndSay {
    public String countAndSay(int n) {
        String lastDesc = null;
        for (int i = 0; i < n; i++) {
            lastDesc = descNumber(lastDesc);
        }
        return String.valueOf(lastDesc);
    }

    String descNumber(String numberStr) {
        if (numberStr == null || numberStr.isEmpty()) {
            return "1";
        }
        char prev = 0;
        int sameCount = 0;

        StringBuilder desc = new StringBuilder();
        for (int i = 0; i < numberStr.length(); i++) {
            if (numberStr.charAt(i) == prev) {
                sameCount += 1;
            }
            else if (prev == 0) {
                prev = numberStr.charAt(i);
                sameCount = 1;
            }
            else {
                desc.append(sameCount).append(prev);
                prev = numberStr.charAt(i);
                sameCount = 1;
            }
        }
        if (sameCount > 0) {
            desc.append(sameCount).append(prev);
        }
        return desc.toString();
    }
}
