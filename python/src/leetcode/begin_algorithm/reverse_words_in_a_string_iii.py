# 202202251400
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/
# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(self.reverse_str(w) for w in s.split(" "))


    def reverse_str(self, string):
        l: List = list(string)
        left, right = 0, len(l) - 1
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        return "".join(l)
