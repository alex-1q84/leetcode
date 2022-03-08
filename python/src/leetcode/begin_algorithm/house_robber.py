# 202203071513
# https://leetcode-cn.com/problems/house-robber/
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(i):
            if i == 0:
                return nums[i]
            elif i == 1:
                return max(nums[0], nums[1])
            else:
                return max(_rob(i-1), _rob(i-2) + nums[i])

        if len(nums) < 2:
            return _rob(len(nums)-1)

        result = 0
        for i in range(2, len(nums)):
            result = max(result, _rob(i))
        return result

print(Solution().rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))
