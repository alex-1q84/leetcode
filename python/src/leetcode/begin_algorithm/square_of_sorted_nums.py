# https://leetcode-cn.com/problems/squares-of-a-sorted-array/
from typing import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 双指针
        low, high = 0, len(nums) - 1
        squares = [0 for i in range(len(nums))]
        for i in range(len(squares) - 1, -1, -1):
            low_square, high_square = pow(nums[low], 2), pow(nums[high], 2)
            if low_square > high_square:
                squares[i] = low_square
                low += 1
            else:
                squares[i] = high_square
                high -= 1
        return squares

print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-7,-3,2,3,11]))
