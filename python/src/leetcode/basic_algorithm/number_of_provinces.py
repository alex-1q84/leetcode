# 202203181732
# https://leetcode-cn.com/problems/number-of-provinces/
# 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
#
# 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
#
# 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
#
# 返回矩阵中 省份 的数量。
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 并查集
        visited = [False for _ in range(len(isConnected))]
        result = 0
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(isConnected, visited, i)
                # print("i={}".format(i))
                # 默认每个城市都不与其他城市相连，所以每个不相连的城市都记为一个省份
                # 通过 dfs 标记直接连接或间接连接的城市，从而正确计数省份
                result += 1
        return result


def dfs(isConnected: List[List[int]], visited: List[bool], i: int):
    for j in range(len(isConnected)):
        # print("i:{}, j:{}, ij:{}, visited:{}".format(i, j, isConnected[i][j], visited[j]))
        if isConnected[i][j] == 1 and not visited[j]:
            visited[j] = True
            dfs(isConnected, visited, j)
