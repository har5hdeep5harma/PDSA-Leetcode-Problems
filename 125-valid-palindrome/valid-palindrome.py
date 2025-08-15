class Solution(object):
    def isPalindrome(self, s):
        a = s.lower().split()
        b = ""
        for word in a:
            for ch in word:
                if ch.isalnum(): 
                    b += ch
        return b == b[::-1]
