# 202203080959
# https://leetcode-cn.com/problems/triangle/
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
# 每一步只能移动到下一行中相邻的结点上。
# 相邻的结点在这里指的是下标与上一层结点下标相同或者等于上一层结点下标+1的两个结点。
# 也就是说，如果正位于当前行的下标i，那么下一步可以移动到下一行的下标i或i+1。
#
# 示例 1：
#
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
# 2
# 3 4
# 6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 动态规划
        # 倒推法，因为要选最短路径，所以从最底层开始每相邻两个两个节点都选最小节点，则倒推回来最终一定是最小值
        dp = [0 for _ in range(len(triangle) + 1)]
        for i in range(len(triangle) - 1, -1, -1):
            for j in (range(len(triangle[i]))):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
            print(triangle[i], dp)
        return dp[0]


print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
