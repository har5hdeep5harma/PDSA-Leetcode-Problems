class Solution(object):    
    def missingNumber(self, nums):
            n = len(nums)
            total = n * (n + 1) // 2   # expected sum of 0..n
            return total - sum(nums)   # missing number