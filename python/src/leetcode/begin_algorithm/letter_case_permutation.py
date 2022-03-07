# 202203071358
# https://leetcode-cn.com/problems/letter-case-permutation/
# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
# 返回 所有可能得到的字符串集合 。以 任意顺序返回输出。
# 例：
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        length = len(s)
        if not length:
            return [""]

        def dfs(start, tmp):
            if start == length or len(tmp) == length:
                res.append(tmp)
                return
            if s[start].isdigit():
                dfs(start+1, tmp + s[start])
            elif s[start].islower():
                dfs(start+1, tmp + s[start])
                dfs(start+1, tmp + s[start].upper())
            elif s[start].isupper():
                dfs(start+1, tmp + s[start])
                dfs(start+1, tmp + s[start].lower())

        dfs(0, "")
        return res

