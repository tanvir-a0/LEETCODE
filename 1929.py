class Solution(object):
    def getConcatenation(self, nums):
        ans = [0 for i in range(len(nums)*2)]
        for i in range(len(nums)):
            ans[i] = nums[i]
        for i in range(len(nums)):
            ans[i + len(nums)] = nums[i]
        
        return ans
        