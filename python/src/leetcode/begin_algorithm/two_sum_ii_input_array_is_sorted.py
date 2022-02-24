# 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列，
# 请你从数组中找出满足相加之和等于目标数 target 的两个数。
# 如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。
#
# 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
#
# 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。
#
# 你所设计的解决方案必须只使用常量级的额外空间。
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 双指针分别指向数组低位和高位
        # 检查两个位置数字之和，如果大于目标值则高位向低位移动 1 个位置，
        # 如果和小于目标值则低位向高位移动一个位置
        # 否则说明和刚好与目标值相等，返回低位和高位
        low, high = 0, len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]
            if sum == target:
                return [low + 1, high + 1]
            elif sum > target:
                high -= 1
            else:
                low += 1
