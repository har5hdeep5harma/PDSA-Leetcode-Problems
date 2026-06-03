class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        se=n*(n+1)
        so=n*n
        m=se
        n=so
        r=m%n

        while(r!=0):
            m=n
            n=r
            r=m%n
        return n
