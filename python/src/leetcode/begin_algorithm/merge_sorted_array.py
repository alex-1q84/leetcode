# 202202251714
# https://leetcode-cn.com/problems/merge-sorted-array/
# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，
# nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 最简单做法是创建一个跟 nums1 同长度数组，用两个分别指向 nums1 和 nums2 的指针，
        # 对比两个指针当前位置值，值小的依次放入新数组，并较小值指针向右移动一位，如此循环，直到其中数组遍历完成
        temp_array = [0 for _ in range(len(nums1))]
        temp_p = 0
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                temp_array[temp_p] = nums1[p1]
                p1 += 1
            else:
                temp_array[temp_p] = nums2[p2]
                p2 += 1
            temp_p += 1
        rest = m - p1
        if rest > 0:
            temp_array[temp_p: temp_p + rest] = nums1[p1: m]
        else:
            rest = n - p2
            if rest > 0:
                temp_array[temp_p:] = nums2[p2: n]
        nums1[:] = temp_array[:]
