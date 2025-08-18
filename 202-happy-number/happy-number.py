class Solution(object):
    def isHappy(self, n, s=None):
        if s==None:
            s=set()
        if n==1:
            return True
        elif n in s:
            return False
        else:
            s.add(n)
        st=str(n)
        sq=0
        for i in range(len(st)):
            sq+=int(st[i])**2
        return self.isHappy(sq, s)
        # s=set()
        # st=str(n)
        # while st not in s:
        #     s.add(st)
        #     sq=0
        #     for i in st:
        #         sq+=int(i)**2
        #     if sq==1:
        #         return True
        #     st=str(sq)
        # return False


