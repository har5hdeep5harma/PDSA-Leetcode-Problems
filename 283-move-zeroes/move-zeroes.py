class Solution(object):
    def moveZeroes(self, nums):
        k=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                k=nums.pop(i)
                nums.append(k)

        return nums