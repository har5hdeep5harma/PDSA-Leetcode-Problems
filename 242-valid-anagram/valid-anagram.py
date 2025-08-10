class Solution(object):
    def isAnagram(self, s, t):
        return list(sorted(s)) == list(sorted(t))
