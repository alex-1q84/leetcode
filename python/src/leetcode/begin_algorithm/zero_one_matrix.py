# 202203021457
# https://leetcode-cn.com/problems/01-matrix/
# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
#
# 两个相邻元素间的距离为 1 。
import collections
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        around_poses = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
        # 广度优先搜索
        row = len(mat)
        col = len(mat[0])
        queue = collections.deque()
        for m in range(row):
            for n in range(col):
                if mat[m][n] == 0:
                    # 记下 0 单元格，这样就可以反过来从 0 单元格找到周边非 0 单元格距当前 0 单元格的距离
                    queue.append((m, n))
                else:
                    # 对非 0 单元格初始化为最远距离
                    mat[m][n] = row + col
        print(mat)
        while queue:
            pos = queue.popleft()
            for v in around_poses:
                r = pos[0] + v[0]
                c = pos[1] + v[1]
                # mat[r][c] > mat[pos[0]][pos[1]] + 1
                # 采用广度优先算法一层层搜索，所以如果上面比较成立就意味着该节点所记录的距离比与当前节点距离要远，
                # 则更新为较近距离
                if 0 <= r < row and 0 <= c < col and mat[r][c] > mat[pos[0]][pos[1]] + 1:
                    mat[r][c] = mat[pos[0]][pos[1]] + 1
                    # 第一轮 0 网格遍历下来，周边的非 0 网格都会获得一个最近 0 节点的距离
                    # 接下来要计算这些非 0 节点周边的非 0 节点距离
                    queue.append((r, c))
        return mat

print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
