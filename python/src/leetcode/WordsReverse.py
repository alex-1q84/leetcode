__author__ = 'mywo'


class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        if not s:
            return s

        words = s.split()
        words.reverse()
        return " ".join(words)