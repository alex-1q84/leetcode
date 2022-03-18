# 202203181620
# https://leetcode-cn.com/problems/number-of-islands/
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
from typing import List


def walk_island(grid: List[List[str]], r: int, c: int):
    if 0 > r or r >= len(grid) or 0 > c or c >= len(grid[r]):
        return
    if grid[r][c] != "1":
        return
    grid[r][c] = "2"
    walk_island(grid, r - 1, c)
    walk_island(grid, r + 1, c)
    walk_island(grid, r, c - 1)
    walk_island(grid, r, c + 1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 深度优先递归遍历岛屿，遍历到的地方都标记上，防止重复遍历
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    islands += 1
                    walk_island(grid, r, c)
        return islands


print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
