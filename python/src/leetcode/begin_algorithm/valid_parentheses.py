# 202202251414
# https://leetcode-cn.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # 栈
        # 如果是 ( 或 { 则压栈，如果是 ) 或 } 则出栈，栈顶元素必定与出栈元素相对，否则认为不成对
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                w = stack.pop()
                if w != pairs[c]:
                    return False
        return len(stack) == 0
