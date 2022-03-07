# 202203071128
# https://leetcode-cn.com/problems/permutations/
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # 回溯
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                # 当前位置之外的数组其他元素
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res
