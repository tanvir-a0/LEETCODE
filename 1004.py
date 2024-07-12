class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        i = 0
        count = 0
        j = 0
        maxxx = 0
        while j < len(nums):
            if nums[j] == 0:
                count = count + 1
            while count > k:
                if nums[i] == 0:
                    count -= 1
                i = i + 1
            j = j + 1
            maxxx = max(maxxx, j - i)
        
        return maxxx
            

        