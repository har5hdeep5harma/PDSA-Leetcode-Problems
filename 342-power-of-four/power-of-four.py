class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        if n==1:
            return True
        while n%4==0:
            n=n//4
            if n==1:
                return True
        return False