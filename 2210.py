class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        for i in range(1,len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                res = res + 1
            
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                res = res + 1
            

        return res
        
