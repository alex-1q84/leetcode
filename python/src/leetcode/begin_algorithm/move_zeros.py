# 2022022405
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从头遍历数组，记录当前有多少个 0 元素 k，把当前非 0 元素向前移动 k 位，最后把数组末尾 k 个位置补上 0
        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i - zero_count] = nums[i]
        nums[len(nums) - zero_count: ] = (0 for _ in range(zero_count))


l = [0, 1, 0, 3, 12]
Solution().moveZeroes(l)
print(l)
l = [0]
print(l)
