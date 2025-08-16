class Solution(object):
    def findLucky(self, arr):
        d={}
        l=[]
        for i in arr:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        for k in d.keys():
            if k==d[k]:
                l.append(k)
        if l:
            max=l[0]
            for n in l:
                if n>=max:
                    max=n
            return max
        else:
            return -1