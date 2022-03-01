# 202202281859
# https://leetcode-cn.com/problems/permutation-in-string/
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
# 提示：s1 和 s2 仅包含小写字母


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 滑动窗口
        # 对 s2 以和 s1 同样宽度的滑动窗口滑动检查每个窗口是否包含 s1 中出现的所有字母
        # 因 s1 和 s2 只包含小写字母，可以统计 s1 中所有字母出现的频率，并保存到一个 dict 中
        # 则检查方法是遍历 s1 的字母频率表并检查是否和 s2 当前窗口字母出现频率相同
        if len(s2) < len(s1):
            return False

        ref_freq = {}
        to_check_freq = {}
        left = 0

        for c in s1:
            ref_freq[c] = ref_freq.get(c, 0) + 1

        for c in s2[left: left + len(s1)]:
            to_check_freq[c] = to_check_freq.get(c, 0) + 1

        for i in range(0, len(s2) - len(s1)):
            if equal_frequency(ref_freq, to_check_freq):
                return True
            else:
                # 只更新左右边界值变化引起的频率变化
                to_check_freq[s2[i]] = to_check_freq.get(s2[i], 0) - 1
                to_check_freq[s2[i + len(s1)]] = to_check_freq.get(s2[i + len(s1)], 0) + 1

        return equal_frequency(ref_freq, to_check_freq)


def equal_frequency(ref_dict, to_check_dict):
    for k, v in ref_dict.items():
        if to_check_dict.get(k, None) != v:
            return False
    return True

