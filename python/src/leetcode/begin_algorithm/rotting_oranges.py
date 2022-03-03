# 202203031127
# https://leetcode-cn.com/problems/rotting-oranges/
# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
#
#     值 0 代表空单元格；
#     值 1 代表新鲜橘子；
#     值 2 代表腐烂的橘子。
#
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
#
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 广度优先
        # 遍历整个网格找出腐烂的橘子放入到队列，遍历这个队列找出腐烂橘子周围的新鲜橘子，
        # 并改变为腐烂橘子，并将其位置加入队列
        # 如此处理直到队列清空
        # 最后检查网格确认还有没有新鲜的橘子
        rot_queue = []
        row = len(grid)
        col = len(grid[0])
        for m in range(row):
            for n in range(col):
                if grid[m][n] == 2:
                    rot_queue.append((m, n))

        times = 0
        around_poses = [(0, -1), (0, +1), (-1, 0), (+1, 0)]
        while rot_queue:
            # 这里之所以要搞一个新的 list 是为了界定一次传染结束
            new_rot_queue = []
            for v in rot_queue:
                for p in around_poses:
                    r, c = v[0] + p[0], v[1] + p[1]
                    if 0 <= r < row and 0 <= c < col and grid[r][c] == 1:
                        grid[r][c] = 2
                        new_rot_queue.append((r, c))
            if not new_rot_queue:
                break
            rot_queue = new_rot_queue[:]
            times += 1

        # 最后检查 grid 确认有无新鲜橘子
        for m in range(row):
            for n in range(col):
                if grid[m][n] == 1:
                    return -1
        return times

