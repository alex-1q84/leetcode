# 202203090935
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/comments/
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 进阶：
#     你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
from typing import List


def find_left_border(nums, target):
    left, right = 0, len(nums) - 1
    left_border = -2
    while left <= right:
        m = left + (right - left) // 2
        if nums[m] >= target:
            # 循环下来找到小于 target 值的最近位置
            right = m - 1
            left_border = right
        else:
            left = m + 1
    return left_border


def find_right_border(nums, target):
    left, right = 0, len(nums) - 1
    right_border = -2
    while left <= right:
        m = left + (right - left) // 2
        if nums[m] > target:
            right = m - 1
        else:
            # 循环下来找到大于 target 值的最近位置
            left = m + 1
            right_border = left
    return right_border


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left_border = find_left_border(nums, target)
        right_border = find_right_border(nums, target)
        print(left_border, right_border)
        if left_border == -2 or right_border == -2:
            return [-1, -1]
        # 因为左右边界分别是小于 target 的最大值和大于 target 的最小值，所以如果左右边界存在则这两个边界的差必然大于 1
        elif right_border - left_border > 1:
            return [left_border + 1, right_border - 1]
        else:
            return [-1, -1]


print(Solution().searchRange([5,7,7,8,8,10], 8))
print(Solution().searchRange([5,7,7,8,8,10], 6))
print(Solution().searchRange([8], 8))
print(find_left_border([0,1,2], 1))
