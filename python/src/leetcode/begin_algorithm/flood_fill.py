# 202203011001
# https://leetcode-cn.com/problems/flood-fill/comments/
# 英文说明更好懂 https://leetcode.com/problems/flood-fill/comments/
# +-+-+-+        +-+-+-+
# |1|1|1|        |2|2|2|
# +-+-+-+        +-+-+-+
# |1|1|0|   ->   |2|2|0|
# +-+-+-+        +-+-+-+
# |1|0|1|        |2|0|2|
# +-+-+-+        +-+-+-+
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 深度优先算法
        oldColor = image[sr][sc]
        dfs(image, sr, sc, oldColor, newColor)
        return image


def dfs(image, sr, sc, oldColor, newColor):
    if sr < 0 or sr >= len(image):
        return image
    if sc < 0 or sc >= len(image[sr]):
        return image
    if image[sr][sc] != oldColor or image[sr][sc] == newColor:
        return image
    image[sr][sc] = newColor
    dfs(image, sr - 1, sc, oldColor, newColor)
    dfs(image, sr + 1, sc, oldColor, newColor)
    dfs(image, sr, sc - 1, oldColor, newColor)
    dfs(image, sr, sc + 1, oldColor, newColor)
