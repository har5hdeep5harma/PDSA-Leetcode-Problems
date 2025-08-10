class Solution(object):
    def isAnagram(self, s, t):
        a=sorted(s)
        b=sorted(t)
        if a==b:
            if sorted(s)==sorted(t):
                return True
        else:
            return False

        