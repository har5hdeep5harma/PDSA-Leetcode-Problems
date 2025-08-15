class Solution(object):
    def isPalindrome(self, s):
        a = s.lower().split()
        b = ""
        for word in a:
            for c in word:
                if c.isalnum(): 
                    b += c
        return b == b[::-1]
