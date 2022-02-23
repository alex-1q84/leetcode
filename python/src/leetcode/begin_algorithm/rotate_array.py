from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 轮转后数据排序还是保持原来一致的，所以只要找到轮转的切换点把这个位置左右两侧的数组拆分对调就行
        split_point = len(nums) - k%len(nums)
        nums[0:k], nums[k:] = nums[split_point:], nums[0:split_point]


l = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(l, 3)
print(l)
l = [-1,-100,3,99]
Solution().rotate(l, 2)
print(l)
