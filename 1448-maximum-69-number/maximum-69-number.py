class Solution(object):
    def maximum69Number (self, num):
        a=list(str(num))
        b=""
        for i in range(len(a)):
            if int(a[i])<9:
                a[i]='9'
                break
        for i in range(len(a)):
            b+=a[i]
        return int(b)