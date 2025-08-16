class Solution(object):
    def largestGoodInteger(self, num):
        l=[]
        if len(num)<3:
            return ""
        for i in range(0,len(num)-2):
            if num[i]==num[i+1]:
                if num[i+1]==num[i+2]:
                    l.append(int(num[i]*3))
        if l:
            max=l[0]
            for j in l:
                if j>=max:
                    max=j
            if max==0:
                return("000")
            return(str(max))
        else:
            return ""