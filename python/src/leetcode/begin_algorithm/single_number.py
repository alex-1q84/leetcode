# 202203081836
# https://leetcode-cn.com/problems/single-number/comments/
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1. 交换律：a ^ b ^ c <=> a ^ c ^ b
        # 2. 任何数于0异或为任何数 0 ^ n => n
        # 3. 相同的数异或为0: n ^ n => 0
        # 所以 a^b^a = a^a^b = 0^b = b
        result = 0
        for n in nums:
            result ^= n
        return result
