class Solution(object):
    def plusOne(self, digits):
        a=""
        l=[]
        for digit in digits:
            a+=str(digit)
        b=int(a)+1
        c=str(b)
        for i in range(len(str(b))):
            l.append(int(c[i]))
        return(l)