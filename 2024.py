class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ct = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if 0 <= i and i < j and j < len(nums):
                    if nums[i] + nums[j] < target:
                        ct = ct + 1
        return ct
        
