# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从数组头开始查找 0 元素，找到 0 元素后则把从这个 0 元素后一位直到数组末尾的所有数字向前移 1 位，
        # 然后把 0 插到队列末尾
        # 继续从原 0 位置向后查找新的 0 元素，该位置不是 0 则向后查找 1 位
        # 重复这个过程
        # 怎么知道已经处理完所有 0 元素？用一个计数器记录已经移动的 0 元素个数，
        # 已经移动的个数加上当前处理到的位置应该等于数组最大索引

        current_index = 0
        zero_count = 0
        while current_index + zero_count != len(nums):
            if nums[current_index] == 0:
                nums[current_index:-1] = nums[current_index+1:]
                nums[-1] = 0
                zero_count += 1
            else:
                current_index += 1


l = [0, 1, 0, 3, 12]
Solution().moveZeroes(l)
print(l)
l = [0]
print(l)
