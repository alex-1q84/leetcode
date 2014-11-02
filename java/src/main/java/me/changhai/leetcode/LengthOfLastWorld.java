package me.changhai.leetcode;

/**
 * Created by bl02515 on 14/11/2.
 */
public class LengthOfLastWorld {
    public int lengthOfLastWord(String s) {
        if(s == null){
            return 0;
        }
        String[] worlds = s.split(" ");
        return worlds.length > 0 ? worlds[worlds.length - 1].length() : 0;
    }
}
