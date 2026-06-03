class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        se=0
        so=0
        for i in range(1,n+1):
            se+=i*2
            so+=(i*2)-1
        m=se if se>so else so
        n=so if se>so else se
        r=m%n

        while(r!=0):
            m=n
            n=r
            r=m%n
        return n
