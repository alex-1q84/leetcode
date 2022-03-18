# 202203181428
# https://leetcode-cn.com/problems/backspace-string-compare/comments/
# 给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。
#
# 注意：如果对空文本输入退格字符，文本继续为空。

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # 双指针
        # 从末尾开始遍历，记录遇到多少个 # 号，直到 # 号用完则比较当前位置字符，
        # 不同则结束比较，相同则继续如此循环，直到遍历完全部字符
        sb, tb = 0, 0
        si, ti = len(s) - 1, len(t) - 1
        while True:
            # 分别循环找到每个字符串最近需要比较的字母
            while si >= 0:
                if s[si] == "#":
                    sb += 1
                elif sb == 0:
                    break
                else:
                    sb -= 1
                si -= 1

            while ti >= 0:
                if t[ti] == "#":
                    tb += 1
                elif tb == 0:
                    break
                else:
                    tb -= 1
                ti -= 1

            if si < 0 or ti < 0:
                break
            if s[si] != t[ti]:
                return False
            else:
                # 双方字符串当前位置字母相同则各自减一位，继续循环比较
                si -= 1
                ti -= 1

        if si == -1 and ti == -1:
            return True
        else:
            return False


print(Solution().backspaceCompare("xywrrmp", "xywrrmu#p"))
