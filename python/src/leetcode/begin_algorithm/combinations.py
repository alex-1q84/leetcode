# 202203071059
# https://leetcode-cn.com/problems/combinations/comments/
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        # 回溯
        def backtrack(n, k, start_index):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start_index, n - (k - len(path)) + 2):
                path.append(i)
                backtrack(n, k, i + 1)
                path.pop()

        backtrack(n, k, 1)
        return res
