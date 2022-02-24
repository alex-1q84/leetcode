# https://leetcode-cn.com/problems/maximum-subarray/
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 定义一个函数f(n)，以第n个数为结束点的子数列的最大和，存在一个递推关系f(n) = max(f(n-1) + A[n], A[n]);
        # 将这些最大和保存下来后，取最大的那个就是，最大子数组和。因为最大连续子数组等价于最大的以n个数为结束点的子数列和 附代码
        max_sum = -pow(10, 4)
        f_n = -1
        for n in nums:
            f_n = max(n, f_n + n)
            max_sum = max(max_sum, f_n)
        return max_sum


    def maxSubArray2(self, nums: List[int]) -> int:
        # 假设sum<=0，那么后面的子序列肯定不包含目前的子序列，
        # 所以令sum = num，如果sum > 0对于后面的子序列是有好处的。
        # res = max(res, sum)保证可以找到最大的子序和。
        res = nums[0]
        sum = 0
        for n in nums:
            if sum > 0:
                sum = sum + n
            else:
                sum = n
            res = max(res, sum)
        return res

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))
