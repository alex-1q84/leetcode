class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        def common_prefix(str_a, str_b):
            global i
            for i, c in enumerate(str_a):
                if i == len(str_b) or c != str_b[i]:
                    return str_a[:i]
            else:
                return str_a[:(i + 1)]

        from functools import reduce
        return reduce(common_prefix, strs)