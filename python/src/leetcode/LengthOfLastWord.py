__author__ = 'mywo'

class Soulution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        try:
            return len(s.split()[-1])
        except:
            return 0
