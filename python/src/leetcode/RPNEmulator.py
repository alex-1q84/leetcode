__author__ = 'mywo'


class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if not tokens:
            raise ValueError("tokens can't be empty")

        rpnStack = [];
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                right = rpnStack.pop()
                left = rpnStack.pop()
                rpnStack.append(calc(left, right, token))
            else:
                rpnStack.append(int(token))
        return
