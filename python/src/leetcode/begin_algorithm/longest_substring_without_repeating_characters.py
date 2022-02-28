# 202202281455
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        # 窗口左侧和右侧位置为 -1 ，当下一个字母没有出现走窗口内，则窗口右边框向右滑动 1 ，
        # 否则左侧边框滑动到第一个重复字母位置，右边框向右滑动 1 （包含当前位置字母），
        # 如此循环，直到右边框位置到达字符串末尾
        left, right = -1, -1
        max_width = 0

        def pos_in_window(c):
            for n in range(left+1, right+1):
                if s[n] == c:
                    return n
            return -1

        for i in range(len(s)):
            pos = pos_in_window(s[i])
            if pos == -1:
                right += 1
                max_width = max(max_width, (right - left))
            else:
                left = pos
                right += 1
        return max_width
