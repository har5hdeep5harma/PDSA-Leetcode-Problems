class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s={}

        for i, n in enumerate(nums):
            if target-n in s:
                return (s[target-n], i)
            s[n]=i