from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def _searchInsert(nums, low, high, target):
            if low == high:
                if target < nums[low]:
                    return low
                if target > nums[low]:
                    return high + 1
                else:
                    return low
            m = middle(low, high)
            if target == nums[m]:
                return m
            elif target > nums[m]:
                return _searchInsert(nums, m+1, high, target)
            else:
                return _searchInsert(nums,low, max(low, m-1), target)
        return _searchInsert(nums, 0, len(nums) - 1, target)


def middle(low, high):
    return low + round((high-low) / 2)

print(Solution().searchInsert([3,5,7,9,10], 8))
print(Solution().searchInsert([1,3], 2))
print(Solution().searchInsert([1,3], 0))
print(Solution().searchInsert([1], 1))
print(Solution().searchInsert([1,3,5,6], 5))
print(Solution().searchInsert([1,3,5,6], 2))
