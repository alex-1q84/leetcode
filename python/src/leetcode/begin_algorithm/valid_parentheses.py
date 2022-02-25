# 202202251414
# https://leetcode-cn.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        # 栈
        # 如果是 ( 或 { 则压栈，如果是 ) 或 } 则出栈，栈顶元素必定与出栈元素相对，否则认为不成对
        # 可能的情况
        # 1. 左括号多出，栈最后不为空
        # 2. 右括号多出，遍历过程中栈空了
        # 3. 左右括号位置不对应，出栈括号跟当前位置括号不成对
        # 4. 括号匹配，遍历后栈为空
        if len(s) % 2 != 0:
            return False

        stack = []
        for c in s:
            if c == '(':
                # 提前把对应的括号压入栈，这样我们就不用在出栈时检查括号映射了，代码更简洁
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif len(stack) == 0 or stack.pop() != c:
                return False
        return len(stack) == 0
