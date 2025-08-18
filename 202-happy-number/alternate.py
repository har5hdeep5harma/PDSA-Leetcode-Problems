class Solution(object):
    def isHappy(self, n, s=None):
      s=set()
        st=str(n)
        while st not in s:
            s.add(st)
            sq=0
            for i in st:
                sq+=int(i)**2
            if sq==1:
                return True
            st=str(sq)
        return False


