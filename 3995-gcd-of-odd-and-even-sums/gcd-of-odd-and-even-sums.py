class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        se=0
        so=0
        for i in range(1,(n*2)+1):
            if i%2==0:
                se+=i
            else:
                so+=i  
        m=se if se>so else so
        n=so if se>so else se
        r=m%n

        while(r!=0):
            m=n
            n=r
            r=m%n
        return n
