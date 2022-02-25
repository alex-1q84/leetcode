# 202202241742
# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
# 找出数组中重复的数字。
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        num_set = set()
        for n in nums:
            if n in num_set:
                return n
            else:
                num_set.add(n)
