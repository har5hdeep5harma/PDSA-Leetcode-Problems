class Solution(object):
    def maximum69Number (self, num):
        a=str(num)
        b=""
        c=True
        for i in range(len(a)):
            if int(a[i])<9 and c:
                b+='9'
                c=False
            else:
                b+=a[i]
        return int(b)