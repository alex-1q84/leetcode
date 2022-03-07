# 202203031532
# https://leetcode-cn.com/problems/add-strings/
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
#
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 采用两个指向两个数组末尾的指针，把指针位置的字符转换为数字并与前一个计算过程得到的进位数字相加，
        # 如此倒序遍历直到较长字符串的末尾
        def _add_strings(long_num: str, short_num: str) -> str:
            long_p, short_p = len(long_num) - 1, len(short_num) - 1
            carry_num = 0

            result = []
            while long_p >= 0:
                current = (carry_num
                           + int(long_num[long_p])
                           + (int(short_num[short_p]) if short_p >= 0 else 0))
                if current < 10:
                    result.append(current)
                    carry_num = 0
                else:
                    carry_num = current // 10
                    current = current % 10
                    result.append(current)
                long_p -= 1
                short_p -= 1
            if carry_num > 0:
                result.append(carry_num)
            return "".join(reversed([str(c) for c in result]))

        if len(num1) > len(num2):
            return _add_strings(num1, num2)
        else:
            return _add_strings(num2, num1)

print(Solution().addStrings("123", "877"))
