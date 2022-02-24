# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
#
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
#
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 分治法
        # 记录【今天之前买入的最小值】
        # 计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
        # 比较【每天的最大获利】，取最大值即可
        min_price, profit = prices[0], 0
        for i, p in enumerate(prices):
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)
        return profit


print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
