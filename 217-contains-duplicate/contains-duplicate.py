class Solution(object):
    def containsDuplicate(self, nums):
        a=set(nums)
        if len(nums)!=len(list(a)):
            return True
        return False