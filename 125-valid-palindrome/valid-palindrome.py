class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=""
        for i in range(len(s)):
            if s[i].isalnum():
                a+=s[i]
        a=a.lower()

        return a==a[::-1]
        