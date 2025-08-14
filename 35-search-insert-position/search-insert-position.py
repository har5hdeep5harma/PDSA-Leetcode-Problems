class Solution(object):
    def searchInsert(self, nums, target):
        k=0
        while(nums[k]<=target and k!=len(nums)-1):
            if nums[k]==target:
                return k
            k+=1
        if k==len(nums)-1:
            if nums[k]==target:
                return k
        if nums[0]>=target:
            return 0
        if nums[k-1]<target and nums[k]>target:
            return k
        if k==len(nums)-1:
            return len(nums)
        