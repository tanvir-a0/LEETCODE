class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)+1):
            dic[i] = 0
        
        for x in nums:
            if x in dic:
                dic[x] = 1
            
        for i in range(len(nums)+1):
            if dic[i] == 0:
                return i
                


        