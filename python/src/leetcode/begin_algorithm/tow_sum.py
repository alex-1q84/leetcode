from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for k, m in enumerate(nums):
                if i != k and nums[i] + nums[k] == target:
                    return [i, k]


print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 6))
