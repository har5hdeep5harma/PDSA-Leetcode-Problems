class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums)!=len(list(set(nums))):
            return True
        return False