class Solution(object):
    def sortedSquares(self, nums):
        # a=list(map(lambda x:x**2,nums))
        
        # return sorted(a)
        return sorted(num * num for num in nums)