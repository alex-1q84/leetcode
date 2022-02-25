# 202202251121
# https://leetcode-cn.com/problems/reverse-string/
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 双指针
        # 设置两个指针分别指向数组头部和尾部，交换这两个指针所对应的数组元素，
        # 然后尾部指针向头移动一位，头部指针向尾移动一位。重复前面这个过程直到尾部指针位置不低于头部指针位置
        left, right = 0, len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
