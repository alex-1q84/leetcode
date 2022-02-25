# 202202251620
# https://leetcode-cn.com/problems/climbing-stairs/comments/
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？


class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        # 设有一个函数 D ，对于第 i 级楼梯，共有 D(i) 种爬法，
        # 第 i-1 级楼梯有 D(i-1) 种爬法，再爬 1 级就是 D(i) 了
        # 第 i-2 级楼梯有 D(i-2) 种爬法，再爬 2 级就是 D(i) 了
        # 所以 D(i) = D(i-1) + D(i-2)
        if n <= 2:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
