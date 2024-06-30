class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count = count + 1
        
        return len(nums) - count
        
s = Solution()
print(s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))