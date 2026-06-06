class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=list(set(nums))
        max=0
        m1=0
        for i in a:
            if nums.count(i)>max:
                m1=i
                max=nums.count(i)
        return(m1)
