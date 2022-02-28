# 202202281455
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        # 窗口左侧位置为 -1 ，当下一个字母没有出现走窗口内，则窗口右边框向右滑动 1 ，
        # 否则左侧边框滑动到第一个重复字母位置，右边框向右滑动 1 （包含当前位置字母），
        # 如此循环，直到右边框位置到达字符串末尾
        # PS: 因为右侧边框总是在当前字母位置，其实可以用当前字母位置代表右边框，从而节省一个变量
        left = -1
        max_width = 0
        last_poses = {}

        for i in range(len(s)):
            left = max(last_poses.get(s[i], -1), left)
            max_width = max(max_width, (i - left))
            last_poses[s[i]] = i
        return max_width
