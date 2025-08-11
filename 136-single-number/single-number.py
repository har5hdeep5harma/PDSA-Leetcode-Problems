class Solution(object):
    def singleNumber(self, nums):
        d={}
        for i in range(len(nums)):
            if nums[i] in d.keys():
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for key in d.keys():
            if d[key]==1:
                return key
        