class Solution(object):
    def minimumOperations(self, nums):
        count = 0
        for x in nums:
            print(x%3)
            if x == 0:
                pass
            if x%3 == 0:
                pass
            if x%3 == 1:
                count = count + 1
            if x%3 == 2:
                count = count + 1
            
        
        return count
