class Solution(object):
    def duplicateZeros(self, arr):
        s=[]
        for a in arr:
            if a==0:
                s.append(0)
                s.append(0)
            else:
                s.append(a)
        for i in range(len(arr)):
            arr[i] = s[i]
