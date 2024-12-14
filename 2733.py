import random

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minn = min(nums)
        maxx = max(nums)



        if minn == maxx:
            if len(nums) == 1:
                return -1

        if len(nums) - 1 - 1 == 0:
            return -1

        x = random.randint(0, len(nums)-1)
        while x in [nums.index(minn), nums.index(maxx)]:
            x = random.randint(0, len(nums)-1)
        
        return nums[x]
        
