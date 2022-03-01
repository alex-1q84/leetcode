# 202203011023
# https://leetcode-cn.com/problems/max-area-of-island/
# 最大岛屿面积
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 深度优先遍历
        max_area = 0
        for m in range(len(grid)):
            for n in range(len(grid[m])):
                if grid[m][n] == 1:
                    max_area = max(max_area, dfs(grid, m, n))
        return max_area


def dfs(grid, m, n):
    if m < 0 or m >= len(grid) or n < 0 or n >= len(grid[m]) or grid[m][n] != 1:
        return 0
    else:
        grid[m][n] = 2
        return (1 + dfs(grid, m - 1, n)
                + dfs(grid, m + 1, n)
                + dfs(grid, m, n - 1)
                + dfs(grid, m, n + 1))
