class Solution(object):
    def containsDuplicate(self, nums):
        a=sorted(nums)
        for i in range(len(nums)-1):
            if a[i]==a[i+1]:
                return True
        return False