# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def _firstBadVerision(low, high):
            if high - low == 1 and isBadVersion(high) and not isBadVersion(low):
                return high
            else:
                m = middle(low, high)
                if isBadVersion(m):
                    return _firstBadVerision(low, m)
                else:
                    return _firstBadVerision(m, high)
        return _firstBadVerision(0, n)


def middle(low, high):
    return low + (high - low) // 2


def isBadVersion(n):
    return n == 4
